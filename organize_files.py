from pathlib import Path
import argparse
import shutil

CATEGORIES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".md"},
    "Spreadsheets": {".csv", ".xls", ".xlsx"},
    "Presentations": {".ppt", ".pptx"},
    "Audio": {".mp3", ".wav", ".m4a"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

def category_for(file_path: Path) -> str:
    suffix = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "Other"

def unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1

def organize(folder: Path, dry_run: bool = False) -> int:
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Not a valid directory: {folder}")

    moved = 0
    for item in folder.iterdir():
        if not item.is_file() or item.name == Path(__file__).name:
            continue

        target_folder = folder / category_for(item)
        target = unique_destination(target_folder / item.name)

        if dry_run:
            print(f"Would move: {item.name} -> {target.relative_to(folder)}")
        else:
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
            print(f"Moved: {item.name} -> {target.relative_to(folder)}")
        moved += 1

    print(f"{'Files that would be moved' if dry_run else 'Files moved'}: {moved}")
    return moved

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Organize files into folders based on file extension."
    )
    parser.add_argument("folder", type=Path, help="Folder to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving any files",
    )
    args = parser.parse_args()

    try:
        organize(args.folder.expanduser().resolve(), args.dry_run)
    except (OSError, ValueError) as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()
