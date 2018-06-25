#!/usr/bin/env python3
# David Omrai, 20.6.2018
# Program for searching empty folders
import os
class Nolder:
    def __init__(self):
        self.visitedFolders = ()
        #self.visitedFolders = list()
        self.mainFolder = self.findDir()
        del self.beBack
        self.homeDir = os.path.abspath(".")
        self.remoteDir = list()
        self.emptyDirs = open("emptyDirs.txt", "a+")
        self.emptyFilesFinder()
    def findDir(self):
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
            self.visitedFolders += os.path.abspath(main),
            #self.visitedFolders.append(os.path.abspath(main))
            os.chdir(main)
            while self.i != 1:
                if os.path.abspath(".") == self.homeDir:
                    self.i = 1
                else:
                    self.remoteDir = self.findDir()
                    del self.beBack
                    if len(os.listdir(".")) == 0:
                        self.emptyDirs.write(os.getcwd()+"\n")
                        os.chdir("..")
                    elif len(self.remoteDir) == 0:
                        os.chdir("..")
                    else:
                        self.visitedFolders += os.path.abspath(self.remoteDir[0]),
                        #self.visitedFolders.append(os.path.abspath(self.remoteDir[0]))
                        os.chdir(self.remoteDir[0])
        self.endMe()
    def endMe(self):
        self.emptyDirs.close()
master = Nolder()
