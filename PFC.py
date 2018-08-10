#!python3

import argparse
from pathlib import Path


def input_path():
    """encapsulates folder selection"""
    folder_path = Path(input("Input path to folder:\n>"))

    if folder_path == "":
        print("No path given, closing...")
        exit(0)

    return folder_path


# command line arguments
def setup_args():
    parser = argparse.ArgumentParser(description='Clean up folders made by Portrait Mode')
    parser.add_argument("--path", help="directory to clean up", default="")

    # read args
    args = parser.parse_args()

    if args.path == "":
        return None

    return Path(args.path)


# clean pathlib object to contain only folders
def get_folders(path):
    folders = []

    for entry in path.iterdir():
        if entry.is_dir():
            folders.append(entry)

    return folders


# --- main ---

print("Welcome to PortraitFolderCleaner (PFC)\n\n")
print("This is going to delete all folders in the target direction, be cautious!")

# 1. Get list of folders

path = setup_args()

if path is None:  # no path in args
    path = input_path()

# TODO remove debug
path = Path(r"E:\TEST")

print(f"Input path: {path}")

# get list of folders

folders = get_folders(path)

confirmation = input(f"folders found: {len(folders)}, continue?[Y]:")

if confirmation != "Y":
    print("Cancelled, goodbye!")
    exit(0)

# iterate over folders and move matching pictures (portraits) to parent directory

for folder in folders:
    for file in folder.glob("*_COVER.jpg"):
        print(f"moving {file}")

        # move .parent

print("\nEverything moved, deleting remaining folders\n")

# Delete folders from drive
for folder in folders:
    print(f"removing {folder}")
    # folder.rmdir()

print("\nDone.\n")
