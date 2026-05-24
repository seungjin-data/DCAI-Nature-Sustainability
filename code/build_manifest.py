"""
build_manifest.py
Generates SHA256 manifest, checksums file, and file tree for the repository.
"""
import hashlib, csv, sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
QC = REPO / "qc_reports"
QC.mkdir(exist_ok=True)

ROLE_MAP = {
    "figures/Figure1": "main_figure",
    "figures/Figure2": "main_figure",
    "figures/Figure3": "main_figure",
    "data/source_data": "source_data",
    "data/supplementary_tables": "supplementary_data",
    "tables/main_tables": "main_table",
    "tables/supplementary_tables": "supplementary_table",
    "supplementary_information": "supplementary_info",
    "code": "reproducibility_code",
    "availability": "availability_statement",
    "release_notes": "release_notes",
    "qc_reports": "qc_report",
}

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def get_role(path):
    for prefix, role in ROLE_MAP.items():
        if str(path).startswith(prefix):
            return role
    return "other"

def run():
    files = sorted([p for p in REPO.rglob("*") if p.is_file() and ".git" not in str(p)])
    rows = []
    checksums = []

    for f in files:
        rel = f.relative_to(REPO)
        h = sha256(f)
        size = f.stat().st_size
        ext = f.suffix.lstrip(".")
        role = get_role(str(rel))
        rows.append({
            "path": str(rel),
            "file_name": f.name,
            "file_type": ext,
            "size_bytes": size,
            "sha256": h,
            "role": role,
            "status": "PRESENT",
        })
        checksums.append(f"{h}  {rel}")

    # Write manifest CSV
    manifest_path = QC / "DCAI_GitHub_Repository_Manifest.csv"
    with open(manifest_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["path","file_name","file_type","size_bytes","sha256","role","status"])
        writer.writeheader()
        writer.writerows(rows)

    # Write checksums
    cksum_path = QC / "DCAI_GitHub_CHECKSUMS_SHA256.txt"
    with open(cksum_path, "w") as f:
        f.write(f"# DCAI Nature Sustainability — SHA256 Checksums\n")
        f.write(f"# Generated: {datetime.now().isoformat()}\n\n")
        f.write("\n".join(checksums))

    # Write file tree
    tree_path = QC / "DCAI_GitHub_FileTree.txt"
    with open(tree_path, "w") as f:
        f.write("DCAI_NatureSustainability/\n")
        for row in rows:
            depth = row["path"].count("/")
            indent = "  " * depth
            f.write(f"{indent}├── {row['file_name']}  ({row['size_bytes']:,}B)\n")

    print(f"\n{'='*60}")
    print("MANIFEST BUILD")
    print(f"{'='*60}")
    print(f"  Files indexed: {len(rows)}")
    print(f"  Manifest:  {manifest_path.relative_to(REPO)}")
    print(f"  Checksums: {cksum_path.relative_to(REPO)}")
    print(f"  File tree: {tree_path.relative_to(REPO)}")
    return True

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
