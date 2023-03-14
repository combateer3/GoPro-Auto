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
    if not source_dir or not os.path.exists(source_dir):
        print("An invalid source directory was provided!")
        sys.exit()
    if not dest_dir or not os.path.exists(dest_dir):
        print("An invalid destination directory was provided!")
        sys.exit()

    # get all video files
    video_files = file_utils.get_source_files(source_dir)

    # extract datetime data from files
    stats = []
    for file in video_files:
        file_data = os.stat(os.path.join(source_dir, file))
        time_data = datetime.fromtimestamp(file_data.st_mtime, tz=timezone(timedelta(hours=EST_HOURS_OFFSET)))
        stats.append(time_data)

        src_file = os.path.join(source_dir, file)
        file_utils.move_file(src_file, dest_dir, time_data)

    # create file structure
    # file_utils.generate_file_structure(stats, dest_dir)


if __name__ == "__main__":
    main(sys.argv[1:])