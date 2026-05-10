#!/usr/bin/env python3
r"""Validate RAG skill files against quality checklist."""

import re
import sys
from pathlib import Path


def parse_frontmatter(content: str) -> dict | None:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end == -1:
        return None
    raw = content[3:end].strip()
    fm = {}

    # Parse key: value pairs
    for line in raw.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("-"):
            key, val = line.split(":", 1)
            key = key.strip().lower()
            val = val.strip().strip('"')
            fm[key] = val
        elif line.startswith("- ") and "allowed-tools" in fm:
            if "tools_list" not in fm:
                fm["tools_list"] = []
            fm["tools_list"].append(line[2:].strip())

    return fm


def get_body(content: str) -> str:
    """Extract content body after frontmatter."""
    if not content.startswith("---"):
        return content
    end = content.find("---", 3)
    if end == -1:
        return content
    return content[end + 3:].strip()


def get_category(path: Path) -> str:
    """Extract category from directory structure."""
    parts = path.parts
    if "skills" not in parts:
        return ""
    idx = parts.index("skills")
    return parts[idx + 1] if idx + 1 < len(parts) else ""


def validate_skill(path: Path) -> list[str]:
    """Validate a single skill file. Returns list of errors/warnings."""
    errors = []
    content = path.read_text(encoding="utf-8")
    lines = content.strip().split("\n")
    line_count = len(lines)
    body = get_body(content)
    fm = parse_frontmatter(content)
    category = get_category(path)

    # --- Frontmatter ---
    if fm is None:
        errors.append(f"FAIL [frontmatter] missing frontmatter delimiters '---'")
        return errors

    # Required frontmatter fields
    if not fm.get("title"):
        errors.append(f"FAIL [frontmatter] missing 'title' field")

    if not fm.get("description"):
        errors.append(f"FAIL [frontmatter] missing 'description' field")

    if not fm.get("category"):
        errors.append(f"FAIL [frontmatter] missing 'category' field")

    if not fm.get("tags"):
        errors.append(f"WARN [frontmatter] missing 'tags' field")

    # --- Description trigger phrases ---
    desc = fm.get("description", "")
    if desc and len(desc) < 30:
        errors.append(f"WARN [description] description too short ({len(desc)} chars, expected 30+)")
    if desc and desc[0].islower():
        errors.append(f"WARN [description] description should start with capital letter")

    # --- allowed-tools ---
    has_tools = "tools_list" in fm
    if not has_tools:
        errors.append(f"WARN [permissions] missing 'allowed-tools' section")

    # --- Required Sections ---
    REQUIRED_SECTIONS = {
        "Overview",
        "Problem Statement",
        "Key Concepts",
        "Implementation Guide",
        "When to Use This Skill",
        "When NOT to Use This Skill",
        "Related Skills",
        "Metrics & Success Criteria",
    }

    # Find all headers (## and ###)
    headers = set(re.findall(r'^#{2,3}\s+(.+)$', body, re.MULTILINE))

    for section in REQUIRED_SECTIONS:
        if section not in headers:
            errors.append(f"WARN [structure] missing section: {section}")

    # --- Implementation Guide should have steps ---
    if "Implementation Guide" in headers:
        step_headers = re.findall(r'^###\s+Step\s+\d+:', body, re.MULTILINE)
        if not step_headers:
            errors.append(f"WARN [implementation] Implementation Guide missing numbered steps (### Step 1:, etc)")

    # --- Related Skills ---
    if "Related Skills" in headers:
        has_links = bool(re.search(r'\[.*?\]\(.*?\.md\)', body))
        if not has_links:
            errors.append(f"WARN [structure] Related Skills section has no skill links")

    # --- Sizing ---
    if line_count < 40:
        errors.append(f"WARN [sizing] only {line_count} lines (expected 40+ for comprehensive skill)")
    elif line_count > 150:
        errors.append(f"WARN [sizing] {line_count} lines (consider splitting into sub-skills)")

    # --- Raw URLs (not wrapped in markdown links) ---
    raw_url_pattern = re.compile(r'(?<!\()(https?://[^\s)]+)(?!\))')
    for i, line in enumerate(lines, 1):
        # skip lines that are already markdown links
        cleaned = re.sub(r'\[.*?\]\(.*?\)', '', line)
        matches = raw_url_pattern.findall(cleaned)
        for url in matches:
            errors.append(f"WARN [formatting] line {i}: raw URL not wrapped in markdown link")
            break

    # --- Bullet consistency (no bullet-point char) ---
    if "\u2022" in body:
        errors.append(f"FAIL [formatting] uses bullet character (•), use '-' instead")

    # --- Em-dash check ---
    if "\u2014" in body:
        errors.append(f"WARN [formatting] contains em-dash character (—), use '--' instead")

    # --- Code block validation ---
    code_blocks = re.findall(r'```(\w*)\n(.*?)```', body, re.DOTALL)
    for lang, block_content in code_blocks:
        if not block_content.strip():
            errors.append(f"WARN [code] empty {lang or 'plain'} code block")

    # --- Category validation ---
    VALID_CATEGORIES = {
        "chunking",
        "vector-databases",
        "retrieval-strategies",
        "data-type-handling",
        "performance-optimization",
        "evaluation-metrics",
        "rag-agents",
        "deployment",
    }
    if category and category not in VALID_CATEGORIES:
        errors.append(f"WARN [category] '{category}' not in valid categories: {', '.join(sorted(VALID_CATEGORIES))}")

    return errors


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate RAG skill files.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (non-zero exit if any warning).",
    )
    args = parser.parse_args()

    skills_dir = Path(__file__).parent.parent / "skills"
    if not skills_dir.exists():
        print(f"error: skills directory not found at {skills_dir}")
        sys.exit(1)

    skill_files = sorted(skills_dir.rglob("SKILL.md"))
    total_errors = 0
    total_warns = 0
    total_pass = 0
    files_with_errors = []

    for path in skill_files:
        rel = path.relative_to(skills_dir.parent)
        errors = validate_skill(path)

        fails = [e for e in errors if e.startswith("FAIL")]
        warns = [e for e in errors if e.startswith("WARN")]

        if not errors:
            print(f"  PASS  {rel}")
            total_pass += 1
        else:
            files_with_errors.append(rel)
            for e in errors:
                prefix = "FAIL" if e.startswith("FAIL") else "WARN"
                print(f"  {prefix}  {rel}: {e.split('] ', 1)[1]}")

        total_errors += len(fails)
        total_warns += len(warns)

    print()
    print(f"results: {len(skill_files)} skills, {total_pass} clean, {total_errors} errors, {total_warns} warnings")

    if files_with_errors:
        print(f"\nskills with issues: {len(files_with_errors)}")
        for f in files_with_errors:
            print(f"  - {f}")

    if total_errors > 0 or (args.strict and total_warns > 0):
        sys.exit(1)


if __name__ == "__main__":
    main()
