import os, sys
from getopt import getopt
from datetime import datetime, timezone, timedelta

from constants import *
import file_utils


def main(argv):
    opts, args = getopt(argv, "v", "verbose")

    for opt, arg in opts:
        if opt in ["-v", "--verbose"]:
            verbose = True
    
    if len(args) < 2:
        print("This script expects two arguments:")
        print("Format: python main.py [options] <source_directory> <destination_directory>")
        sys.exit()

    source_dir = args[0]
    dest_dir = args[1]
    if not source_dir or not os.path.exists(source_dir):
        print("An invalid source directory was provided!")
        sys.exit()
    if not dest_dir or not os.path.exists(dest_dir):
        print("An invalid destination directory was provided!")
        sys.exit()

    # get all video files
    video_files = file_utils.get_source_files(source_dir)

    # extract datetime data from files
    moved_files = 0
    for file in video_files:
        src_file = os.path.join(source_dir, file)
        file_data = os.stat(src_file)
        time_data = datetime.fromtimestamp(file_data.st_mtime, tz=timezone(timedelta(hours=EST_HOURS_OFFSET)))

        # move file to destination
        file_utils.move_file(src_file, dest_dir, time_data, verbose=verbose)
        moved_files += 1

    if verbose:
        print(f"\n{moved_files} total files were moved!")

    input("Press any key to continue...")


if __name__ == "__main__":
    main(sys.argv[1:])