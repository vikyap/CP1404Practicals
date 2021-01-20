import os
import shutil


def main():
    source = "FilesToSort"
    file_list = os.listdir(source)

    for file in file_list:
        if os.path.isdir(file):
            pass
        extension = file.split(".")[-1]
        if os.path.exists(source + '/' + extension):
            shutil.move(source + '/' + file, source + '/' + extension + '/' + file)
        else:
            os.mkdir(source + "/" + extension)
            shutil.move(source + '/' + file, source + '/' + extension + "/" + file)

main()
