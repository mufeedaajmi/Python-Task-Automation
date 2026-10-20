# Python Task Automation

A small Python command-line tool that organizes files into folders based on file extension.

## Features
- Groups common file types into categories such as Images, Documents, Videos, and Archives
- Places unknown extensions in an `Other` folder
- Avoids overwriting files by generating a unique destination name
- Includes a `--dry-run` option to preview actions safely

## Requirements
- Python 3.9 or later
- No third-party packages

## Usage

Preview changes first:

```bash
python organize_files.py "/path/to/test-folder" --dry-run
```

Run the organizer:

```bash
python organize_files.py "/path/to/test-folder"
```

Replace the example path with a folder you own and want to organize. Test on a temporary folder first and keep a backup of important files.

## Concepts demonstrated
Path handling with `pathlib`, command-line arguments with `argparse`, functions, dictionaries, loops, and file operations with `shutil`.

## Future improvements
- Add logging to a file
- Add configurable file categories
- Write unit tests with `unittest`
