from datetime import datetime
import os


def generate_file_structure(file_data: datetime, dest_dir: str) -> None:
    year = file_data.year
    month = file_data.month
    day = file_data.day

    path = f"{year}/{month}/{day}"
    if not os.path.exists(path):
        os.makedirs(path)


class FileData:
    def __init__(self) -> None:
        pass