import os
import shutil


def main():
    source = "FilesToSort"
    file_list = os.listdir(source)
    category = {}

    for file in file_list:
        if os.path.isdir(file):
            pass
        extension = file.split(".")[-1]

