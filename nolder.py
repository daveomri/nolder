# David Omrai, 20.6.2018
# Program for searching empty folders
import os
def nolder():
    preMainFolder = list(map(lambda x: x if(os.path.isdir(x) == True) else None, os.listdir(".")))
    mainFolder = list()
    for file in preMainFolder:
        if file != None: mainFolder.append(file)
        else: pass
    homeDir = os.path.abspath(".")
    remDir = list()
    nameMainFolder = os.getcwd()
    visitedFolders = list()
    listZero = []
    print("I'm working on it.")
    for main in mainFolder:
        i = 0
        os.chdir(main)
        visitedFolders.append(main)
        while i != 1:
            if os.path.abspath(".") == homeDir:
                i = 1
            else:
                remDir = list(map(lambda x: x if(os.path.isdir(x) == True) else "file", os.listdir(".")))
                dirDirs = list()
                for file in remDir:
                    if file != "file" and (os.path.abspath(file) in visitedFolders) == False:
                        dirDirs.append(file)
                    else: pass
                if len(remDir) == 0:
                    visitedFolders.append(os.getcwd())
                    listZero.append(os.getcwd())
                    os.chdir("..")
                elif len(dirDirs) == 0:
                    visitedFolders.append(os.getcwd())
                    os.chdir("..")
                else:
                    visitedFolders.append(os.path.abspath(dirDirs[0]))
                    os.chdir(os.path.abspath(dirDirs[0]))
    print(listZero)
nolder()
