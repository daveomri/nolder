#!/usr/bin/env python3
# David Omrai, 20.6.2018
# Program for searching empty folders
import os, time, sys
class Nolder:
    def __init__(self):
        self.timeProgram = time.time()
        self.visitedFolders = set()
        self.dupliFiles = dict()
        self.homeDir = os.getcwd()
        self.remoteCloud = ()
        self.Iminwhat = ""
        self.lambdaDupliDir = lambda x: [x.split(".")[-1], os.path.abspath(x)]
        self.whatToDo()
    def whatToDo(self):
        command = input("What to do?(emptyDirs/emptyFiles/duplicates): ")
        while command not in ("emptyDirs", "emptyFiles", "duplicates"):
            command = input("Choose one of them -> (emptyDirs/emptyFiles/duplicates): ")
        if command == "emptyDirs":
            self.emptyDirsFinder()
        elif command = "emptyFiles":
            self.emptyFilesFinder()
        else:
            self.duplicatesFinder()
    def findType(self, whereyouare=None, inside=()):
        if whereyouare == self.Iminwhat and len(inside) > 0:
            inside = list(inside)
            del inside[0]
            inside = tuple(inside)
        else:
            inside = ()
            info = list(map(lambda x: "dir" if(os.path.isdir(x) == True) else ("file" if(os.path.isfile(x) == True) else "idk"), os.listdir(".")))
            for i in range(len(info)):
                if (os.path.abspath(os.listdir(".")[i]) in self.visitedFolders) != True:
                    if info[i] in ("dir", "file"):
                        inside += [info[i], os.listdir(".")[i]],
                    else: pass
                else: pass
        return inside
    def emptyFilesFinder(self):
        print("We are working on it..")
        self.mainFolder = self.findType()
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
                        self.remoteCloud = self.findType(os.getcwd(), self.remoteCloud)
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
        print(str((time.time()-self.timeProgram)/60))
        self.endMe(self.emptyFiles)
    def duplicatesFinder(self):
        infoHolder = None
        self.dupliFilesLogger = open("dupliFiles.txt", "a+")
        self.dupliFilesLogger.write("Hello, there are locacions of empty files, have a nice day!\n")
        self.mainFolder = os.listdir(".")
        print("I'm working on it")
        for main in self.mainFolder:
            if os.path.isdir(main) == True:
                os.chdir(main)
                self.visitedFolders.add(os.path.abspath(main))
                i = 0
                while i == 0:
                    if os.path.abspath(".") == self.homeDir:
                        self.visitedFolders = set()
                        i = 1
                    else:
                        self.remoteCloud = self.findType(os.path.abspath("."), self.remoteCloud)
                        if len(self.remoteCloud) == 0:
                            self.visitedFolders.add(os.path.abspath("."))
                            os.chdir("..")
                        else:
                            if self.remoteCloud[0][0] == "file":
                                self.Iminwhat = os.path.abspath(".")
                                if os.stat(self.remoteCloud[0][1]).st_size in self.dupliFiles:
                                    infoHolder = self.lambdaDupliDir(self.remoteCloud[0][1])
                                    print(infoHolder)
                                    print(self.dupliFiles[os.stat(self.remoteCloud[0][1]).st_size], "\n\n")

                                    if infoHolder[0] == self.dupliFiles[os.stat(self.remoteCloud[0][1]).st_size][0]:
                                        self.dupliFilesLogger.write(os.path.abspath(self.remoteCloud[0][1])+"\n"+self.dupliFiles[os.stat(self.remoteCloud[0][1]).st_size][-1]+"\n\n\n\n");
                                    else:
                                        self.dupliFiles[os.stat(self.remoteCloud[0][1]).st_size] = self.lambdaDupliDir(self.remoteCloud[0][1])
                                else:
                                    self.dupliFiles[os.stat(self.remoteCloud[0][1]).st_size] = self.lambdaDupliDir(self.remoteCloud[0][1])
                            else:

                                os.chdir(self.remoteCloud[0][1])
                            self.visitedFolders.add(os.path.abspath(self.remoteCloud[0][1]))
            else:
                if os.stat(main).st_size in self.dupliFiles:
                    infoHolder = self.lambdaDupliDir(main)
                    print(infoHolder)
                    print(self.dupliFiles[os.stat(main).st_size], "\n\n")
                    if infoHolder[0] == self.dupliFiles[os.stat(main).st_size][0]:
                        self.dupliFilesLogger.write(os.path.abspath(main)+"\n"+self.dupliFiles[os.stat(main).st_size][-1]+"\n\n\n\n");
                    else:
                        self.dupliFiles[os.stat(main).st_size] = self.lambdaDupliDir(main)
                else:
                    self.dupliFiles[os.stat(main).st_size] = self.lambdaDupliDir(main)
        self.endMe(self.dupliFilesLogger)
    def emptyDirsFinder(self):
        def findDir():
            beBack = list()
            checkDir = list(map(lambda x: x if(os.path.isdir(x) == True) else None, os.listdir(".")))
            for file in checkDir:
                if file != None and (os.path.abspath(file) in self.visitedFolders) == False:
                    beBack.append(file)
                else: pass
            return beBack
        self.emptyDirs = open("emptyDirs.txt", "w")
        self.mainFolder = findDir()
        print("I'm working on it..")
        for main in self.mainFolder:
            i = 0
            self.visitedFolders.add(os.path.abspath(main))
            os.chdir(main)
            while i != 1:
                if os.path.abspath(".") == self.homeDir:
                    i = 1
                else:
                    self.remoteCloud = findDir(os.path.abspath("."), self.remoteCloud)
                    if len(os.listdir(".")) == 0:
                        self.emptyDirs.write(os.getcwd()+"\n")
                        os.chdir("..")
                    elif len(self.remoteCloud) == 0:
                        os.chdir("..")
                    else:
                        self.visitedFolders.add(os.path.abspath(self.remoteCloud[0]))
                        os.chdir(self.remoteCloud[0])
        self.endMe(self.emptyDirs)
    def endMe(self, closeThis):
        closeThis.close()
master = Nolder()
