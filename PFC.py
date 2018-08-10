#!python3

from pathlib import Path
import argparse


def input_path():
    """encapsulates folder selection"""
    folder_path = Path(input("Input path to folder:\n>"))

    if folder_path == "":
        print("Goodbye")
        exit(0)

    return folder_path


# command line arguments
def setup_args():
    parser = argparse.ArgumentParser(description='Clean up folders made by Portrait Mode')
    parser.add_argument("--path", help="directory to clean up", default="")

    # read args
    args = parser.parse_args()

    return args.path

# --- main ---

print("Welcome to PortraitFolderCleaner (PFC)\n\n")

# 1. Get list of folders

path = setup_args()

if path == "":
    path = input_path()



# 2. Delete empty folders from list and drive

# 3. iterate over folders and move matching pictures (portraits) to parent directory

