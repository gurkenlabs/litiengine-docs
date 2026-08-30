import re
import sys
from pathlib import Path

def lint_markdown():
    root = Path(__file__).resolve().parent.parent.parent
    docs_dir = root / "docs"
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        sys.exit(1)
        
    md_files = list(docs_dir.rglob("*.md"))
    errors = []
    
    for f in md_files:
        rel = f.relative_to(root).as_posix()
        text = f.read_text(encoding="utf-8")
        
        # 1. Check Frontmatter
        if not text.startswith("---"):
            errors.append(f"{rel}: Missing YAML frontmatter header (---)")
            
        lines = text.splitlines()
        in_code = False
        fence_char = ""
        fence_line = 0
        
        for idx, line in enumerate(lines):
            line_num = idx + 1
            stripped = line.strip()
            
            # 2. Check Code Fences
            if stripped.startswith("```") or stripped.startswith("~~~"):
                if not in_code:
                    in_code = True
                    fence_char = stripped[:3]
                    fence_line = line_num
                    tag = stripped[3:].strip()
                    if not tag and stripped.startswith("```"):
                        errors.append(f"{rel}:{line_num}: Unlabeled code fence (missing language tag)")
                else:
                    if stripped.startswith(fence_char):
                        in_code = False
                        
            if in_code:
                continue
                
            # 3. Check List Boundaries (Must have blank line before starting list from paragraph)
            is_list_item = stripped.startswith("* ") or stripped.startswith("- ") or bool(re.match(r'^\d+\.\s', stripped))
            if is_list_item and idx > 0:
                prev_line = lines[idx - 1].strip()
                prev_is_list = prev_line.startswith("* ") or prev_line.startswith("- ") or bool(re.match(r'^\d+\.\s', prev_line))
                prev_is_empty = (prev_line == "")
                prev_is_heading = prev_line.startswith("#")
                prev_is_fence = prev_line.startswith("```") or prev_line.startswith("~~~")
                prev_is_admonition = prev_line.startswith("!!!") or prev_line.startswith("???")
                prev_is_html = prev_line.startswith("<") or prev_line.endswith(">")
                prev_is_card = "markdown" in prev_line or "cards" in prev_line
                
                if not prev_is_list and not prev_is_empty and not prev_is_heading and not prev_is_fence and not prev_is_admonition and not prev_is_html and not prev_is_card:
                    errors.append(f"{rel}:{line_num}: List item without preceding blank line after paragraph: '{prev_line[:40]}'")

            # 4. Check Table Boundaries (Must have blank line before table header)
            is_table_row = stripped.startswith("|") and stripped.endswith("|")
            if is_table_row and idx + 1 < len(lines):
                next_line = lines[idx + 1].strip()
                if re.match(r'^\|[\s:-|-]+\|$', next_line) and idx > 0:
                    prev_line = lines[idx - 1].strip()
                    prev_is_table = prev_line.startswith("|") and prev_line.endswith("|")
                    if not prev_is_table and prev_line != "" and not prev_line.startswith("#") and not prev_line.startswith("<"):
                        errors.append(f"{rel}:{line_num}: Table header without preceding blank line: '{prev_line[:40]}'")
                    
        if in_code:
            errors.append(f"{rel}:{fence_line}: Unclosed code fence opened on line {fence_line}")

    if errors:
        print(f"Markdown Syntax Lint Failed with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"All markdown syntax and list formatting checks passed ({len(md_files)} files verified)!")
        sys.exit(0)

if __name__ == "__main__":
    lint_markdown()
