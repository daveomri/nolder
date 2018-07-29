#!usr/bin/env python3
# David Omrai, 28.7.2018
from nolder import Nolder
import time, os

# This function defines which way wants user go
def whatMode():
    master = Nolder()
    homeDir = input("Locacion: ")
    while os.path.isdir(homeDir) == False:
        homeDir = homeDir = input("Locacion: ")
    master.homeDir = homeDir
    command = None
    while command not in ("emptyDirs", "emptyFiles", "duplicates"):
        command = input("Choose one of them -> (emptyDirs/emptyFiles/duplicates): ")
        if command == "emptyDirs":
            master.emptyDirsFinder()
        elif command == "emptyFiles":
            master.emptyFilesFinder()
        else:
            master.filesType = input("What type of files? (text/video/audio/photo): ")
            while master.filesType not in master.dictTypes:
                master.filesType = input("What type of files? (text/video/audio/photo): ")
            master.duplicatesFinder()
    nowWhat = input("Where should I store outcome? (print/file): ")
    while nowWhat not in {"print", "file"}:
        nowWhat = input("Where should I store outcome? (print/file): ")
    if nowWhat == "print":
        print(master.logger)
        for i in master.logger:
            print(i)
    else:
        iamHere = "/".join(os.path.realpath(__file__).split("/")[0:-1])
        file = open(iamHere+"/outcome.txt", "w")
        for i in master.logger:
            file.write(i+"\n\n")
        file.close()
    print(os.path.realpath(__file__))
if __name__ == "__main__":
    whatMode()
