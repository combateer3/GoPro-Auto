import os, sys
from datetime import datetime, timezone, timedelta

from constants import *
import file_utils


def main(argv):
    if len(argv) < 2:
        print("This script expects two arguments:")
        print("Format: python main.py <source_directory> <destination_directory>")
        sys.exit()

    source_dir = argv[0]
    dest_dir = argv[1]
    if not source_dir:
        print("An invalid source directory was provided!")
    if not dest_dir:
        print("An invalid destination directory was provided!")

    # set given directory
    os.chdir(source_dir)
    # get file statistics
    result = os.stat("R:\GoPro Auto\drop\GX010126.mp4")
    print(result)
    # creates a datetime object for EST
    modified = datetime.fromtimestamp(result.st_mtime, tz=timezone(timedelta(hours=EST_HOURS_OFFSET)))

    # create file structure
    file_utils.generate_file_structure(modified, dest_dir)


if __name__ == "__main__":
    main(sys.argv[1:])