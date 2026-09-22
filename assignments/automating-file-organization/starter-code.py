from pathlib import Path
import argparse
import shutil


CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".docx", ".txt", ".md"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Videos": {".mp4", ".mov", ".avi"},
}


def category_for(file_path: Path) -> str:
    """Return the category for a file based on its extension."""
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def unique_destination(destination: Path) -> Path:
    """Return an available path without replacing an existing file."""
    candidate = destination
    counter = 1
    while candidate.exists():
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        counter += 1
    return candidate


def organize_files(
    source: Path,
    destination: Path,
    dry_run: bool = False,
) -> dict[str, int]:
    """Organize files from source into category folders."""
    if not source.is_dir():
        raise ValueError(f"Source folder does not exist: {source}")

    summary: dict[str, int] = {}
    for file_path in source.iterdir():
        if not file_path.is_file():
            continue

        category = category_for(file_path)
        category_folder = destination / category
        target = unique_destination(category_folder / file_path.name)
        print(f"{file_path} -> {target}")

        if not dry_run:
            category_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(target))

        summary[category] = summary.get(category, 0) + 1

    return summary


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Organize files by category")
    parser.add_argument("source", type=Path, help="Folder containing the files")
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path("organized"),
        help="Folder where category folders will be created",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned moves without changing files",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    try:
        summary = organize_files(
            arguments.source,
            arguments.destination,
            arguments.dry_run,
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error

    print("Summary:")
    for category, count in sorted(summary.items()):
        print(f"- {category}: {count}")


if __name__ == "__main__":
    main()