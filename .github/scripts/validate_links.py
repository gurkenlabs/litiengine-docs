import re
import sys
from pathlib import Path

def validate_links():
    root = Path(__file__).resolve().parent.parent.parent
    docs_dir = root / "docs"
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        sys.exit(1)
        
    md_files = list(docs_dir.rglob("*.md"))
    broken_links = []
    broken_images = []
    
    # 1. Collect all valid markdown files and anchor slugs
    file_headings = {}
    for f in md_files:
        rel = f.relative_to(docs_dir).as_posix()
        text = f.read_text(encoding="utf-8")
        headings = re.findall(r'^#{1,6}\s+(.+)$', text, flags=re.MULTILINE)
        anchors = set()
        for h in headings:
            slug = re.sub(r'[^\w\s-]', '', h.lower()).strip().replace(' ', '-')
            slug = re.sub(r'[-\s]+', '-', slug)
            anchors.add(slug)
        file_headings[rel] = anchors

    # 2. Audit all markdown links
    for f in md_files:
        rel = f.relative_to(docs_dir).as_posix()
        text = f.read_text(encoding="utf-8")
        
        # Strip code blocks
        text_no_code = re.sub(r'```[\s\S]*?```', '', text)
        text_no_code = re.sub(r'`[^`]+`', '', text_no_code)
        
        # Image links
        for alt, img_path in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text_no_code):
            img_path = img_path.strip().split()[0]
            if not img_path.startswith("http://") and not img_path.startswith("https://") and not img_path.startswith("data:"):
                if img_path.startswith("/"):
                    target_img = docs_dir / img_path.lstrip("/")
                else:
                    target_img = (f.parent / img_path).resolve()
                if not target_img.exists():
                    broken_images.append(f"{rel}: Missing image reference '{img_path}'")

        # Document links
        for label, link_url in re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', text_no_code):
            link_url = link_url.strip().split()[0]
            if link_url.startswith("http://") or link_url.startswith("https://") or link_url.startswith("mailto:"):
                continue
                
            url_parts = link_url.split("#")
            doc_part = url_parts[0]
            anchor_part = url_parts[1] if len(url_parts) > 1 else None
            
            if doc_part:
                if doc_part.startswith("/"):
                    target_file = (docs_dir / doc_part.lstrip("/")).resolve()
                else:
                    target_file = (f.parent / doc_part).resolve()
                    
                if not target_file.exists():
                    if (target_file.parent / (target_file.name + ".md")).exists():
                        target_file = target_file.parent / (target_file.name + ".md")
                    elif (target_file / "index.md").exists():
                        target_file = target_file / "index.md"
                    elif (target_file / "README.md").exists():
                        target_file = target_file / "README.md"
                    else:
                        broken_links.append(f"{rel}: Dead link target '{link_url}' (File does not exist: {target_file})")

    if broken_links or broken_images:
        print(f"Link Validation Failed with {len(broken_links) + len(broken_images)} issue(s):")
        for b in broken_links:
            print(f"  ❌ {b}")
        for img in broken_images:
            print(f"  🖼️ {img}")
        sys.exit(1)
    else:
        print(f"All {len(md_files)} markdown files have 100% valid internal links and image references!")
        sys.exit(0)

if __name__ == "__main__":
    validate_links()
