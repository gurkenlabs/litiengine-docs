import re
import sys
from pathlib import Path

def lint_markdown():
    root = Path(__file__).resolve().parent.parent.parent
    docs_dir = root / "docs"
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        sys.exit(1)
        
    md_files = [f for f in docs_dir.rglob("*.md") if "assets" not in f.parts]
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

            # 5. Check Admonition Indentation (Line following !!! or ??? must be indented with 4 spaces)
            if re.match(r'^[!?]{3}\s+[a-zA-Z0-9_-]+', stripped) and idx + 1 < len(lines):
                next_line = lines[idx + 1]
                if next_line.strip() and not next_line.startswith("    "):
                    errors.append(f"{rel}:{line_num+1}: Admonition content must be indented by 4 spaces: '{next_line[:40]}'")
                    
        if in_code:
            errors.append(f"{rel}:{fence_line}: Unclosed code fence opened on line {fence_line}")

        # 6. Check Content Tab Block Indentation (All lines inside === "..." tab blocks must have >= 4 spaces)
        in_tab = False
        tab_start_line = 0
        in_tab_fence = False
        for idx, line in enumerate(lines):
            line_num = idx + 1
            stripped = line.strip()
            
            if re.match(r'^===\s+"[^"]+"', stripped):
                in_tab = True
                tab_start_line = line_num
                in_tab_fence = False
                continue
                
            if in_tab:
                if stripped.startswith("```") or stripped.startswith("~~~"):
                    in_tab_fence = not in_tab_fence
                    if not line.startswith("    "):
                        errors.append(f"{rel}:{line_num}: Code fence inside tab block must be indented by 4 spaces (tab opened on line {tab_start_line})")
                    continue
                    
                if not in_tab_fence and (line.startswith("#") or line.startswith("---") or line.startswith("<div") or line.startswith("</div")):
                    in_tab = False
                    continue
                    
                if stripped == "":
                    continue
                    
                if not line.startswith("    "):
                    errors.append(f"{rel}:{line_num}: Content inside tab block must be indented by at least 4 spaces: '{line[:40]}' (tab opened on line {tab_start_line})")

        # 7. Check for Raw UTF-8 Emojis (Disallowed - use native SVG icons :material-...: or clean text)
        emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]|[\u2600-\u27BF]|[\u2300-\u23FF]|[\u2B50-\u2B55]')
        for idx, line in enumerate(lines):
            line_num = idx + 1
            # Skip code blocks for unicode tests if necessary, but ban in prose/headers
            match = emoji_pattern.search(line)
            if match and not line.strip().startswith("```") and "assets" not in rel:
                errors.append(f"{rel}:{line_num}: Raw UTF-8 emoji '{match.group(0)}' found. Use native Material/Lucide SVG icons instead.")

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
