#!/usr/bin/env python3
"""
============================================================
  📁 Project Tree Generator
============================================================
  Generate a visual tree structure of your project.
  
  Usage:
      python generate_tree.py
  
  Creates a README.md file with your project's file structure.
  Use .treeignore to exclude files/folders (like .gitignore)
============================================================
"""

import os
from datetime import datetime


# ──────────────────────────────────────────────
# DEFAULT IGNORE PATTERNS
# ──────────────────────────────────────────────
DEFAULT_IGNORE_DIRS  = {".git", "__pycache__", ".venv", "venv", "node_modules", ".idea", ".vscode", ".next", "dist", "build"}
DEFAULT_IGNORE_FILES = {".DS_Store", "Thumbs.db", "generate_tree.py", "__init__.py"}


# ──────────────────────────────────────────────
# LOAD .treeignore
# ──────────────────────────────────────────────
def load_treeignore(root: str) -> tuple[set, set]:
    """
    Load exclusion patterns from .treeignore file
    Returns (ignore_dirs, ignore_files)
    """
    ignore_file_path = os.path.join(root, ".treeignore")
    ignore_dirs = DEFAULT_IGNORE_DIRS.copy()
    ignore_files = DEFAULT_IGNORE_FILES.copy()
    
    if os.path.exists(ignore_file_path):
        try:
            with open(ignore_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    
                    # Directories end with /
                    if line.endswith("/"):
                        ignore_dirs.add(line.rstrip("/"))
                    else:
                        ignore_files.add(line)
        except Exception:
            pass
    
    return ignore_dirs, ignore_files


# ──────────────────────────────────────────────
# GENERATE TREE STRUCTURE
# ──────────────────────────────────────────────
def generate_tree(root: str, ignore_dirs: set, ignore_files: set) -> list[str]:
    """
    Generate visual tree structure of the project
    Returns a list of lines representing the tree
    """
    tree_lines = []
    
    for dirpath, dirnames, filenames in os.walk(root):
        # Filter ignored directories
        dirnames[:] = sorted(d for d in dirnames if d not in ignore_dirs)

        level = dirpath.replace(root, "").count(os.sep)
        indent = "│   " * level
        folder_name = os.path.basename(dirpath)

        if level == 0:
            tree_lines.append(f"📁 {folder_name}/")
        else:
            tree_lines.append(f"{indent}📁 {folder_name}/")

        subindent = "│   " * (level + 1)
        for fname in sorted(filenames):
            if fname in ignore_files:
                continue
            
            ext = os.path.splitext(fname)[1].lower()

            # Icons by file extension
            icons = {
                # Code
                ".py": "🐍", ".js": "📜", ".ts": "📘", ".jsx": "⚛️", ".tsx": "⚛️",
                ".java": "☕", ".cpp": "⚙️", ".c": "⚙️", ".h": "📋", ".cs": "🔷",
                ".go": "🐹", ".rs": "🦀", ".php": "🐘", ".rb": "💎", ".swift": "🍎",
                
                # Web
                ".html": "🌐", ".css": "🎨", ".scss": "🎨", ".sass": "🎨",
                ".vue": "💚", ".svelte": "🧡",
                
                # Data
                ".json": "📋", ".xml": "📋", ".yaml": "⚙️", ".yml": "⚙️",
                ".toml": "📄", ".ini": "⚙️", ".cfg": "⚙️", ".conf": "⚙️",
                
                # Database
                ".sql": "🗄️", ".db": "🗄️", ".sqlite": "🗄️",
                
                # Documents
                ".md": "📝", ".txt": "📄", ".pdf": "📕", ".doc": "📘", ".docx": "📘",
                
                # Scripts
                ".sh": "💻", ".bash": "💻", ".zsh": "💻", ".ps1": "💻",
                
                # Docker
                ".dockerfile": "🐳",
                
                # Other
                ".env": "🔐", ".gitignore": "🚫", ".lock": "🔒",
                ".jpg": "🖼️", ".jpeg": "🖼️", ".png": "🖼️", ".gif": "🖼️", ".svg": "🎨",
            }
            
            icon = icons.get(ext, "📄")
            
            # Special files
            if fname.lower() == "dockerfile":
                icon = "🐳"
            elif fname.lower() == "readme.md":
                icon = "📖"
            elif fname.lower() == "license":
                icon = "⚖️"
            elif fname.lower() in ("makefile", "cmake", "rakefile"):
                icon = "🔨"
            elif fname.lower().startswith(".git"):
                icon = "🔧"
            
            tree_lines.append(f"{subindent}{icon} {fname}")

    return tree_lines


# ──────────────────────────────────────────────
# GENERATE README
# ──────────────────────────────────────────────
def generate_readme(project_name: str, tree_lines: list[str]) -> str:
    """
    Generate README.md content with the project tree
    """
    lines = []
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    lines.append(f"# 📁 {project_name}")
    lines.append("")
    lines.append("> Project structure documentation")
    lines.append(f"> *Generated automatically on {now}*")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    lines.append("## 🗂️ Project Structure")
    lines.append("")
    lines.append("```")
    lines.extend(tree_lines)
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Statistics
    total_items = len(tree_lines)
    folders = sum(1 for line in tree_lines if "📁" in line)
    files = total_items - folders
    
    lines.append("## 📊 Statistics")
    lines.append("")
    lines.append(f"- **Total items:** {total_items}")
    lines.append(f"- **Folders:** {folders}")
    lines.append(f"- **Files:** {files}")
    lines.append("")
    
    return "\n".join(lines)


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    root = os.getcwd()
    project_name = os.path.basename(root)
    
    print("=" * 70)
    print("  📁 PROJECT TREE GENERATOR")
    print("=" * 70)
    print(f"Project: {project_name}")
    print(f"Path: {root}")
    print()
    
    # Load ignore patterns
    ignore_dirs, ignore_files = load_treeignore(root)
    
    # Generate tree
    print("🔍 Scanning project structure...")
    tree_lines = generate_tree(root, ignore_dirs, ignore_files)
    print(f"   ✅ {len(tree_lines)} items found")
    
    # Generate README
    readme_content = generate_readme(project_name, tree_lines)
    
    # Write to file
    output_path = os.path.join(root, "README.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print()
    print("=" * 70)
    print(f"✅ README.md generated successfully!")
    print("=" * 70)
    print(f"📝 File: {output_path}")
    print(f"📏 Lines: {len(readme_content.splitlines())}")
    print()


if __name__ == "__main__":
    main()