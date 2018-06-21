#!/usr/bin/env python3
# David Omrai, 20.6.2018
# Program for searching empty folders
import os
class Nolder:
    def __init__(self):
        self.visitedFolders = list()
        self.mainFolder = self.findDir()
        del self.beBack
        self.homeDir = os.path.abspath(".")
        self.remoteDir = list()
        self.emptyDirs = list()
        self.emptyFilesFinder()
    def findDir(self):
        """
        self.bin = list()
        for numfile in range(len(os.listdir("."))):
            if os.path.isdir(os.listdir(".")[numfile]) == True and (os.path.abspath(os.listdir(".")[numfile]) in self.visitedFolders) == False:
                self.bin.append(os.listdir(".")[numfile])
            else:
                pass
        return self.bin
        """
        self.beBack = list()
        checkDir = list(map(lambda x: x if(os.path.isdir(x) == True) else None, os.listdir(".")))
        for file in checkDir:
            if file != None and (os.path.abspath(file) in self.visitedFolders) == False:
                self.beBack.append(file)
            else:
                pass
        return self.beBack

    def emptyFilesFinder(self):
        print("I'm working on it..")
        for main in self.mainFolder:
            self.i = 0
            self.visitedFolders.append(os.path.abspath(main))
            os.chdir(main)
            while self.i != 1:
                if os.path.abspath(".") == self.homeDir:
                    self.i = 1
                else:
                    self.remoteDir = self.findDir()
                    del self.beBack
                    if len(os.listdir(".")) == 0:
                        self.emptyDirs.append(os.getcwd())
                        os.chdir("..")
                    elif len(self.remoteDir) == 0:
                        os.chdir("..")
                    else:
                        self.visitedFolders.append(os.path.abspath(self.remoteDir[0]))
                        os.chdir(self.remoteDir[0])
        self.endMe()
    def endMe(self):
        print(self.emptyDirs)
"""
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
"""
Nolder()
#nolder()
