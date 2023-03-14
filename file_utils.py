from datetime import datetime
from typing import List
import os, shutil


# gets all video files from source directory
def get_source_files(source_dir: str) -> List[str]:
    # get all files in directory
    files = []
    for f in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, f)):
            files.append(f)

    # filter mp4 and lrv files
    return list(filter(is_gopro_file, files))


# all gopro files start with GL or GX and are mp4 or lrv files
# this is based on the Hero 11 format
def is_gopro_file(file: str) -> bool:
    file = file.lower()
    if not file.startswith("gx") and not file.startswith("gl"):
        return False
    
    if not file.endswith(".mp4") and not file.endswith(".lrv"):
        return False
    
    return True


# moves source file to destination file and renames if necessary.
# paths should be absolute to be consistent
def move_file(source_file: str, dest_dir: str, time_data: datetime, verbose=False) -> None:
    # create folder structure based on datetime object
    file_structure = time_data.strftime("%Y/%B/%d %a")

    # get the file name by itself
    file_name = os.path.basename(os.path.normpath(source_file))
    proxy = file_name.startswith("GL")

    # create the destination directory
    subfolder = "Proxies" if proxy else "Full" # different folders for actual files and proxies
    final_dest = os.path.join(dest_dir, file_structure, subfolder)
    if not os.path.exists(final_dest):
        os.makedirs(final_dest)

    final_dest = os.path.join(final_dest, file_name)

    if verbose:
        print(f"Moving {source_file} to {final_dest}")

    # move the file
    shutil.move(source_file, final_dest)