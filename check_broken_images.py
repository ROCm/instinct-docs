#!/usr/bin/env python3
"""
Lint check for broken image references in documentation.

This script scans all markdown files in the docs directory and verifies that:
1. All referenced images exist in the filesystem
2. Image paths are correctly formatted
3. No orphaned images exist (optional check)
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Set


class ImageChecker:
    """Check for broken image references in markdown documentation."""

    def __init__(self, docs_dir: str = "docs"):
        self.docs_dir = Path(docs_dir)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.checked_files = 0
        self.checked_images = 0

    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files in the docs directory."""
        md_files = []
        for ext in ["*.md", "*.rst"]:
            md_files.extend(self.docs_dir.rglob(ext))
        return sorted(md_files)

    def extract_image_references(self, file_path: Path) -> List[Tuple[str, int]]:
        """
        Extract all image references from a markdown file.
        
        Returns list of tuples: (image_path, line_number)
        """
        image_refs = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            self.errors.append(f"Error reading {file_path}: {e}")
            return []

        # Pattern 1: MyST grid card syntax - :img-top: path
        img_top_pattern = re.compile(r':img-top:\s+(.+?)(?:\s|$)')
        
        # Pattern 2: Standard markdown - ![alt](path) or ![alt](path "title")
        md_pattern = re.compile(r'!\[.*?\]\(([^\s\)"]+)')
        
        # Pattern 3: HTML img tags - <img src="path"> or <img src='path'>
        html_pattern = re.compile(r'<img[^>]+src=["\'"]([^"\']+)["\'"]')
        
        # Pattern 4: reStructuredText image directive
        rst_pattern = re.compile(r'\.\.\s+image::\s+(.+?)(?:\s|$)')
        
        # Pattern 5: reStructuredText figure directive
        rst_figure_pattern = re.compile(r'\.\.\s+figure::\s+(.+?)(?:\s|$)')

        for line_num, line in enumerate(lines, start=1):
            # Check all patterns
            for pattern in [img_top_pattern, md_pattern, html_pattern, rst_pattern, rst_figure_pattern]:
                matches = pattern.findall(line)
                for match in matches:
                    # Clean up the path
                    img_path = match.strip()
                    # Remove surrounding quotes if present
                    if (img_path.startswith('"') and img_path.endswith('"')) or \
                       (img_path.startswith("'") and img_path.endswith("'")):
                        img_path = img_path[1:-1]
                    # Skip URLs
                    if img_path.startswith(('http://', 'https://', '//')):
                        continue
                    # Skip data URIs
                    if img_path.startswith('data:'):
                        continue
                    image_refs.append((img_path, line_num))

        return image_refs

    def resolve_image_path(self, md_file: Path, img_ref: str) -> Path:
        """
        Resolve relative image path to absolute path.
        
        Args:
            md_file: Path to the markdown file
            img_ref: Image reference from the markdown file
        
        Returns:
            Resolved absolute path
        """
        # Get the directory containing the markdown file
        md_dir = md_file.parent
        
        # Resolve the image path relative to the markdown file
        img_path = (md_dir / img_ref).resolve()
        
        return img_path

    def check_file(self, md_file: Path) -> None:
        """Check all image references in a single markdown file."""
        self.checked_files += 1
        image_refs = self.extract_image_references(md_file)
        
        for img_ref, line_num in image_refs:
            self.checked_images += 1
            img_path = self.resolve_image_path(md_file, img_ref)
            
            # Get relative path for error messages
            try:
                rel_md_path = md_file.relative_to(Path.cwd())
            except ValueError:
                rel_md_path = md_file
            
            if not img_path.exists():
                self.errors.append(
                    f"{rel_md_path}:{line_num}: Broken image reference: '{img_ref}' "
                    f"(resolved to: {img_path})"
                )
            elif not img_path.is_file():
                self.errors.append(
                    f"{rel_md_path}:{line_num}: Image path is not a file: '{img_ref}' "
                    f"(resolved to: {img_path})"
                )

    def find_orphaned_images(self) -> Set[Path]:
        """
        Find images in the images directory that are not referenced anywhere.
        
        Returns:
            Set of orphaned image paths
        """
        # Find all image files
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp'}
        all_images = set()
        
        images_dir = self.docs_dir / 'images'
        if images_dir.exists():
            for img_file in images_dir.rglob('*'):
                if img_file.is_file() and img_file.suffix.lower() in image_extensions:
                    all_images.add(img_file)
        
        # Find all referenced images
        referenced_images = set()
        md_files = self.find_markdown_files()
        
        for md_file in md_files:
            image_refs = self.extract_image_references(md_file)
            for img_ref, _ in image_refs:
                img_path = self.resolve_image_path(md_file, img_ref)
                if img_path.exists():
                    referenced_images.add(img_path.resolve())
        
        # Find orphaned images
        orphaned = all_images - referenced_images
        return orphaned

    def run(self, check_orphans: bool = False) -> int:
        """
        Run the image checker.
        
        Args:
            check_orphans: Whether to check for orphaned images
        
        Returns:
            Exit code (0 for success, 1 for errors)
        """
        print(f"Checking images in {self.docs_dir}...")
        print()
        
        md_files = self.find_markdown_files()
        
        if not md_files:
            print(f"No markdown files found in {self.docs_dir}")
            return 1
        
        # Check each file
        for md_file in md_files:
            self.check_file(md_file)
        
        # Check for orphaned images if requested
        if check_orphans:
            orphaned = self.find_orphaned_images()
            for img in sorted(orphaned):
                try:
                    rel_path = img.relative_to(Path.cwd())
                except ValueError:
                    rel_path = img
                self.warnings.append(f"Orphaned image (not referenced): {rel_path}")
        
        # Print results
        print(f"Checked {self.checked_files} markdown files")
        print(f"Checked {self.checked_images} image references")
        print()
        
        if self.errors:
            print(f"❌ Found {len(self.errors)} broken image reference(s):")
            print()
            for error in self.errors:
                print(f"  {error}")
            print()
        
        if self.warnings:
            print(f"⚠️  Found {len(self.warnings)} warning(s):")
            print()
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if not self.errors and not self.warnings:
            print("✅ All image references are valid!")
            return 0
        elif not self.errors:
            print("✅ All image references are valid (warnings only)")
            return 0
        else:
            return 1


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Check for broken image references in documentation"
    )
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Documentation directory to check (default: docs)"
    )
    parser.add_argument(
        "--check-orphans",
        action="store_true",
        help="Also check for orphaned images (images not referenced anywhere)"
    )
    
    args = parser.parse_args()
    
    checker = ImageChecker(args.docs_dir)
    exit_code = checker.run(check_orphans=args.check_orphans)
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
