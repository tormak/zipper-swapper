import zipfile
import json
import os
import sys

from zipper_config import *

print("Welcome to Zipper, simple tool for replacing existing files in zip \
archive.")

if 4 != len(sys.argv):
    print("Wrong argument list")
    exit()

read_config()

first_filesize = config['first_file_filesize']
secod_filesize = config['second_file_filesize']

first_filename  = sys.argv[1]
second_filename = sys.argv[2]
zip_filename    = sys.argv[3]

if not zipfile.is_zipfile(zip_filename):
    print("Zip doesn't exist")
    exit()

with zipfile.ZipFile(zip_filename, 'a') as file_zip:
    with file_zip.getinfo(first_filename) as first_in_zip:
        print(first_in_zip.file_size)
        if first_in_zip.file_size == first_filesize:
            file_zip.write(first_filename)
