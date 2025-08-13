# scripts/gen_auto_indexes.py
import os
from pathlib import Path
import mkdocs_gen_files

DOCS_DIR = Path("docs")

def ensure_index_for(dir_path: Path):
    rel = dir_path.relative_to(DOCS_DIR)
    # skip hidden or special dirs
    parts = rel.parts
    if any(p.startswith(".") or p.startswith("_") for p in parts):
        return
    index_md = dir_path / "index.md"
    if not index_md.exists():
        # virtual write: file is generated at build time; it won't touch your repo
        with mkdocs_gen_files.open(str(rel / "index.md"), "w") as f:
            title = rel.name.replace("-", " ").title() if rel.name else "Home"
            f.write(f"# {title}\n\n")
            f.write("This index page was generated automatically.\n\n")
            f.write("## Contents\n\n")
            # list children pages/folders
            for child in sorted(dir_path.iterdir()):
                if child.is_dir():
                    name = child.name.replace("-", " ").title()
                    f.write(f"- [{name}]({child.name}/)\n")
                elif child.suffix.lower() in {".md", ".markdown", ".mdown", ".mkdn", ".mkd"} and child.name != "index.md":
                    f.write(f"- [{child.stem.replace('-', ' ').title()}]({child.name})\n")

def walk_and_index(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        ensure_index_for(Path(dirpath))

if __name__ == "__main__":
    walk_and_index(DOCS_DIR)
