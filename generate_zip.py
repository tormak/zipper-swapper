import zipfile
import sys

with zipfile.ZipFile('test.zip', 'a') as file_zip:
    file_zip.write('12.txt')
    file_zip.write('2')
