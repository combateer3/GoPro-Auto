# GoPro Auto

## Description
GoPro Auto is a simple Python 3 script that can be used to sort GoPro files into folders by recording date. Given a source directory, the script searches for files in the GoPro format and reads the metadata to create folders by year, month, and day. Within each dated folder, the recordings will be separated into full resolution and proxy files.

This script assumes the [GoPro Hero 11 naming convention](https://community.gopro.com/s/article/GoPro-Camera-File-Naming-Convention?language=en_US).

## Format
The script uses the following commandline format:

    python main.py [options] <source directory> <destination directory>

The given paths should be absolute paths.

### Options
The only current supported option is verbose: `-v` or `--verbose`