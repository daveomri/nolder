#!/usr/bin/env python3
# David Omrai, 20.6.2018
# Program for searching empty folders
import os, time
class Nolder:
    def __init__(self):
        self.timeProgram = time.time()
        self.visitedFolders = set()
        #self.visitedFolders = list()
        self.homeDir = os.getcwd()
        self.remoteCloud = ()
        self.Iminwhat = ""
        self.emptyFilesFinder()
    def findDir(self):
        beBack = list()
        checkDir = list(map(lambda x: x if(os.path.isdir(x) == True) else None, os.listdir(".")))
        for file in checkDir:
            if file != None and (os.path.abspath(file) in self.visitedFolders) == False:
                beBack.append(file)
            else:
                pass
        return beBack
    def emptyFilesFinder(self):
        print("We are working on it..")
        def findType(whereyouare=None, inside=()):
            if whereyouare == self.Iminwhat and len(inside) > 0:
                inside = list(inside)
                del inside[0]
                inside = tuple(inside)
            else:
                inside = ()
                info = list(map(lambda x: "dir" if(os.path.isdir(x) == True) else "file", os.listdir(".")))
                for i in range(len(info)):
                    if (os.path.abspath(os.listdir(".")[i]) in self.visitedFolders) != True:
                        inside += [info[i], os.listdir(".")[i]],
                    else:
                        pass
            return inside
        self.mainFolder = findType()
        self.emptyFiles = open("emptyFiles.txt", "a+")
        self.emptyFiles.write("Hello, there are locacions of empty files, have a nice day!\n")
        self.routingFile = None
        for number in self.mainFolder:
            if number[0] == "dir":
                i = 0
                os.chdir(number[1])
                while i != 1:
                    if os.getcwd() == self.homeDir:
                        self.visitedFolders = set()
                        i = 1
                    else:
                        self.remoteCloud = findType(os.getcwd(), self.remoteCloud)
                        if len(self.remoteCloud) == 0:
                            self.visitedFolders.add(os.getcwd())
                            os.chdir("..")
                        else:
                            if self.remoteCloud[0][0] == "file":
                                self.routingFile = os.stat(self.remoteCloud[0][1]).st_size
                                if self.routingFile == 0:
                                    self.emptyFiles.write(os.path.abspath(self.remoteCloud[0][1])+"\n")
                                else:
                                    pass
                                self.Iminwhat = os.getcwd()
                            else:
                                os.chdir(self.remoteCloud[0][1])
                            self.visitedFolders.add(os.path.abspath(self.remoteCloud[0][1]))
            else:
                self.routingFile = os.stat(number[1]).st_size
                if self.routingFile == 0:
                    self.emptyFiles.write(os.path.abspath(number[1]))
                else:
                    pass
        self.emptyFiles.close()
        print(str((time.time()-self.timeProgram)/60))
    def emptyDirsFinder(self):
        self.emptyDirs = open("emptyDirs.txt", "a+")
        self.mainFolder = self.findDir()
        print("I'm working on it..")
        for main in self.mainFolder:
            i = 0
            self.visitedFolders.add(os.path.abspath(main))
            #self.visitedFolders.append(os.path.abspath(main))
            os.chdir(main)
            while i != 1:
                if os.path.abspath(".") == self.homeDir:
                    i = 1
                else:
                    self.remoteCloud = self.findDir()
                    if len(os.listdir(".")) == 0:
                        self.emptyDirs.write(os.getcwd()+"\n")
                        os.chdir("..")
                    elif len(self.remoteCloud) == 0:
                        os.chdir("..")
                    else:
                        self.visitedFolders.add(os.path.abspath(self.remoteCloud[0]))
                        #self.visitedFolders.append(os.path.abspath(self.remoteCloud[0]))
                        os.chdir(self.remoteCloud[0])
        self.endMe()
    def endMe(self):
        self.emptyDirs.close()
master = Nolder()
