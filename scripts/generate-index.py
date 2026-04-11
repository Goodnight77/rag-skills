#!/usr/bin/env python3
"""
Generate index files for the rag-skills repository.

This script generates:
1. INDEX.md - A browsable index of all skills
2. SKILLS.json - A JSON index for programmatic access
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class SkillInfo:
    """Information about a skill."""
    id: str
    title: str
    category: str
    tags: List[str]
    author: str
    last_updated: str
    file_path: str
    relative_path: str
    description: str

class SkillIndexer:
    """Index all skills in the repository."""

    def __init__(self, root_dir: str = None):
        """Initialize indexer."""
        self.root_dir = Path(root_dir) if root_dir else Path(__file__).parent.parent
        self.skills: List[SkillInfo] = []
        self.categories: Dict[str, List[SkillInfo]] = {}

    def index_all(self) -> bool:
        """Index all skill files."""
        print(f"Indexing skills in: {self.root_dir}")
        print("-" * 60)

        # Find all skill files
        skill_files = self._find_skill_files()

        print(f"Found {len(skill_files)} skill files\n")

        # Index each file
        for skill_file in skill_files:
            skill_info = self._index_file(skill_file)
            if skill_info:
                self.skills.append(skill_info)

        # Build category index
        self._build_indexes()

        # Generate outputs
        self._generate_markdown_index()
        self._generate_json_index()

        print(f"\nGenerated index for {len(self.skills)} skills")

        return True

    def _find_skill_files(self) -> List[Path]:
        """Find all native SKILL.md files in skills/ directory."""
        skills_dir = self.root_dir / "skills"
        if not skills_dir.exists():
            print("ERROR skills/ directory not found")
            return []

        return sorted(skills_dir.rglob("SKILL.md"))

    def _index_file(self, file_path: Path) -> SkillInfo:
        """Extract metadata from a skill file."""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            print(f"WARN Could not read: {file_path.name}")
            return None

        # Extract frontmatter
        metadata = self._extract_frontmatter(content)

        if not metadata:
            print(f"WARN No frontmatter in: {file_path.name}")
            return None

        # Extract description from overview
        description = self._extract_description(content)

        # Get relative path
        relative_path = file_path.relative_to(self.root_dir)

        # Create skill info
        skill_id = metadata.get('title', file_path.stem).lower().replace(' ', '-')

        return SkillInfo(
            id=metadata.get('name', skill_id),
            title=metadata.get('title', ''),
            category=metadata.get('category', ''),
            tags=self._parse_tags(metadata.get('tags', '')),
            author=metadata.get('author', ''),
            last_updated=metadata.get('last_updated', ''),
            file_path=str(file_path),
            relative_path=relative_path.as_posix(),
            description=description
        )

    def _extract_frontmatter(self, content: str) -> Dict[str, str]:
        """Extract and parse frontmatter."""
        if not content.startswith("---"):
            return {}

        end_delimiter = content.find("---", 4)
        if end_delimiter == -1:
            return {}

        frontmatter = content[4:end_delimiter]

        fields = {}
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip().strip('"\'')
                fields[key] = value

        return fields

    def _parse_tags(self, tags_str: str) -> List[str]:
        """Parse tags from frontmatter string."""
        if tags_str.startswith('[') and tags_str.endswith(']'):
            import ast
            try:
                return ast.literal_eval(tags_str)
            except:
                return [t.strip() for t in tags_str[1:-1].split(',') if t.strip()]
        return [t.strip() for t in tags_str.split(',') if t.strip()]

    def _extract_description(self, content: str) -> str:
        """Extract description from Overview section."""
        # Find Overview section
        overview_match = re.search(
            r'## Overview\s*\n+(.+?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )

        if overview_match:
            desc = overview_match.group(1).strip()
            # Take first sentence or first 150 chars
            desc = re.sub(r'\s+', ' ', desc)  # Normalize whitespace

            if '.' in desc:
                first_sentence = desc.split('.')[0] + '.'
                if len(first_sentence) > 300:
                    return desc[:250] + "..."
                return first_sentence

            return desc[:250] + "..."

        return ""

    def _build_indexes(self):
        """Build category index."""
        for skill in self.skills:
            # Category index
            if skill.category not in self.categories:
                self.categories[skill.category] = []
            self.categories[skill.category].append(skill)

    def _generate_markdown_index(self):
        """Generate INDEX.md file."""
        index_path = self.root_dir / "INDEX.md"

        content = "# RAG Skills Index\n\n"
        content += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        content += f"Total Skills: {len(self.skills)}\n\n"
        content += "---\n\n"

        # Browse by Category
        content += "## Browse by Category\n\n"
        for category, skills in sorted(self.categories.items()):
            content += f"### {category.replace('-', ' ').title()}\n\n"
            for skill in skills:
                content += f"- [{skill.title}]({skill.relative_path})\n"
                content += f"  - *{skill.description}*\n"
            content += "\n"

        # All Skills
        content += "## All Skills\n\n"
        content += "| Title | Category | Tags |\n"
        content += "|-------|----------|------|\n"
        for skill in sorted(self.skills, key=lambda s: s.title):
            tags_display = ", ".join(skill.tags[:3])
            if len(skill.tags) > 3:
                tags_display += f" (+{len(skill.tags) - 3})"
            content += f"| [{skill.title}]({skill.relative_path}) | {skill.category} | {tags_display} |\n"

        index_path.write_text(content, encoding='utf-8')
        print("Generated INDEX.md")

    def _generate_json_index(self):
        """Generate SKILLS.json file."""
        json_path = self.root_dir / "SKILLS.json"

        index_data = {
            "generated": datetime.now().isoformat(),
            "total_skills": len(self.skills),
            "categories": {k: len(v) for k, v in self.categories.items()},
            "skills": [
                {
                    "id": skill.id,
                    "title": skill.title,
                    "category": skill.category,
                    "tags": skill.tags,
                    "author": skill.author,
                    "last_updated": skill.last_updated,
                    "description": skill.description,
                    "path": skill.relative_path
                }
                for skill in self.skills
            ]
        }

        json_path.write_text(
            json.dumps(index_data, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        print("Generated SKILLS.json")

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate index files for RAG skills")
    parser.add_argument(
        "--root-dir",
        type=str,
        default=None,
        help="Root directory of rag-skills repository"
    )

    args = parser.parse_args()

    indexer = SkillIndexer(args.root_dir)
    success = indexer.index_all()

    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
