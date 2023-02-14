import os, shutil
from datetime import datetime, timezone, timedelta

from constants import *


def main():
    full_path = f"{os.getcwd()}/{DEFAULT_FOLDER}"
    os.chdir(full_path)
    # get file statistics
    result = os.stat("GX010126.mp4")
    print(result)
    # creates a datetime object for EST
    modified = datetime.fromtimestamp(result.st_mtime, tz=timezone(timedelta(hours=EST_HOURS_OFFSET)))
    print(modified)


if __name__ == "__main__":
    main()