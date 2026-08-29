import sys
import re
from pathlib import Path

def lint():
    root = Path(__file__).resolve().parent.parent.parent
    md_files = [f for f in root.rglob("*.md") if f.name not in ["SUMMARY.md", "AGENTS.md"] and ".github" not in str(f)]
    
    errors = []
    
    for f in md_files:
        rel = f.relative_to(root)
        text = f.read_text(encoding="utf-8", errors="replace")
        
        # 1. Check Frontmatter
        if not text.startswith("---"):
            errors.append(f"Missing frontmatter in {rel}")
            
        # 2. Check Code Fence Tags
        lines = text.splitlines()
        in_code = False
        for idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("```"):
                if not in_code:
                    tag = stripped[3:].strip()
                    if not tag:
                        errors.append(f"Unlabeled code fence in {rel} on line {idx + 1}")
                    in_code = True
                else:
                    in_code = False

    # 3. Check SUMMARY.md duplicates
    summary_path = root / "SUMMARY.md"
    if summary_path.exists():
        summary_text = summary_path.read_text(encoding="utf-8")
        links = re.findall(r'\[([^\]]+)\]\((/docs/[^)]+)\)', summary_text)
        seen = set()
        for title, link in links:
            if link in seen:
                errors.append(f"Duplicate link in SUMMARY.md: [{title}]({link})")
            seen.add(link)

    if errors:
        print(f"Documentation Lint Failed with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"All documentation checks passed successfully ({len(md_files)} markdown files checked)!")
        sys.exit(0)

if __name__ == "__main__":
    lint()
