from datetime import datetime
from typing import List
import os


# gets all video files from source directory
def get_source_files(source_dir: str) -> List[str]:
    # get all files in directory
    files = []
    for f in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, f)):
            files.append(f)

    # filter mp4 and lrv files
    return list(filter(lambda f: f.lower().endswith(".mp4") or f.lower().endswith(".lrv"), files))


# create file structure based on date time objects
def generate_file_structure(file_data: List[datetime], dest_dir: str) -> None:
    os.chdir(dest_dir)
    
    for file in file_data:
        path = file.strftime("%Y/%B/%d %a")

        if not os.path.exists(path):
            os.makedirs(path)