#!/usr/bin/env python3
# David Omrai, 20.6.2018
# Program for searching empty folders, empty files and duplicates
import os, sys
class Nolder:
    def __init__(self):
        # Declaring of class variables
        self.visitedFolders = set()
        self.dupliFiles = dict()
        self.homeDir = os.getcwd()
        self.logger = set()
        self.filesType = None
        self.remoteCloud = ()
        self.Iminwhat = ""
        self.dictTypes = {"text":{"txt", "doc"}, "audio": {"mp3", "wav", "otg"}, "video": {"mp4", "wav", "avi"}, "photo":{"jpeg", "JPEG", "png", "PNG", "TIFF", "bmp", "BMP", "GIF", "gif", "svg", "SVG"}}
        self.lambdaDupliDir = lambda x: [x.split(".")[-1], os.path.abspath(x)] # split the type of file (.jpeg, .png, etc..), get absolute path of this file
    # Function that saves a little amount of space here, also prevent program from getting the permission error -> in case you run it without super user rights
    def changeDirNoLoop(self, where, fullwhere):
        if len(where.split(".")) > 1 or " " and ")" and "(" in where or "current" == where:
            pass
        else:
            try:
                os.chdir(fullwhere)
            except (PermissionError): pass
        self.visitedFolders.add(fullwhere)
    # Main purpose of this function is finding correct items and returning them back
    def findType(self, whatToFind = (), whereyouare=None, inside=()):# whatToFind derlares what we're looking for, if files, dirs or both
        # if the program location is equal to where I was before, and there're still some files, do this
        if whereyouare == self.Iminwhat and len(inside) > 0:
            inside = list(inside)
            del inside[0] # Delete first item in list named inside and transform it back to tuple-> that's where program is
            inside = tuple(inside)
        else:
            inside = () # we're in a new dir, program has changed its location, therefore we've to know where we was before -> wwhich dirs or files we want to avoid
            try:
                info = list(map(lambda x: "dir" if(os.path.isdir(x) == True) else ("file" if(os.path.isfile(x) == True) else "idk"), os.listdir(".")))
            except (PermissionError):
                info = ()
            try:
                for i in range(len(info)):
                    if os.path.abspath(os.listdir(".")[i]) not in self.visitedFolders:
                        if info[i] in whatToFind:
                            inside += [info[i], os.listdir(".")[i]],
                        else: pass
                    else: pass
            except: pass
        return inside
    # No words are needed to guess the purpose of this function -> it finds empty Files
    def emptyFilesFinder(self):
        os.chdir(self.homeDir)
        self.mainFolder = self.findType(("dir", "file"))
        self.routingFile = None
        for number in self.mainFolder:
            if number[0] == "dir":
                i = 0
                self.changeDirNoLoop(number[1], os.path.abspath(number[1]))
                while i != 1:
                    if os.getcwd() == self.homeDir:
                        self.visitedFolders = set()
                        i = 1
                    else:
                        self.remoteCloud = self.findType(("dir", "file"), os.getcwd(), self.remoteCloud)
                        if len(self.remoteCloud) == 0:
                            self.visitedFolders.add(os.getcwd())
                            os.chdir("..")
                        else:
                            if self.remoteCloud[0][0] == "file":
                                self.routingFile = os.stat(self.remoteCloud[0][1]).st_size
                                if self.routingFile == 0:
                                    self.logger.add(os.path.abspath(self.remoteCloud[0][1]))
                                    #self.emptyFiles.write(os.path.abspath(self.remoteCloud[0][1])+"\n")
                                else: pass
                                self.Iminwhat = os.getcwd()
                                self.visitedFolders.add(os.path.abspath(self.remoteCloud[0][1]))
                            else:
                                self.changeDirNoLoop(self.remoteCloud[0][1], os.path.abspath(self.remoteCloud[0][1]))
            else:
                self.routingFile = os.stat(number[1]).st_size
                if self.routingFile == 0:
                    self.logger.add(os.path.abspath(number[1]))
                    #self.emptyFiles.write(os.path.abspath(number[1]))
                else: pass
        self.endMe()#self.emptyFiles
    # Function: I'll find all of them, those who have the same identity
    def duplicatesFinder(self):
        def fileChecker(what):
            self.Iminwhat = os.path.abspath(".")
            if typesOfFiles(what) == True:
                if os.stat(what).st_size in self.dupliFiles: # if the same size of file is in directory, go this way
                    infoHolder = self.lambdaDupliDir(what) # get info about this file (what type and full location)
                    #print(infoHolder)
                    #print(self.dupliFiles[os.stat(what).st_size], "\n\n")
                    if infoHolder[0] == self.dupliFiles[os.stat(what).st_size][0]: # if types are equal
                        self.dupliFiles[os.stat(what).st_size][1] += "\n"+infoHolder[1]
                        #self.logger.add(os.path.abspath(what)+"\n"+self.dupliFiles[os.stat(what).st_size][-1])
                        #self.dupliFilesLogger.write(os.path.abspath(what)+"\n"+self.dupliFiles[os.stat(what).st_size][-1]+"\n\n\n\n"); # match, I found you dupli-one
                    else: self.dupliFiles[os.stat(what).st_size] = self.lambdaDupliDir(what)
                else: # if not, than append this file to directory
                    self.dupliFiles[os.stat(what).st_size] = self.lambdaDupliDir(what)
            else: pass
            self.visitedFolders.add(os.path.abspath(what))
        os.chdir(self.homeDir)
        infoHolder = None
        typesOfFiles = lambda x: True if(x.split(".")[-1] in self.dictTypes[self.filesType]) else (True if(self.filesType == "text" and len(x.split(".")) == 1) else False)
        self.mainFolder = self.findType(("dir", "file"))
        for main in self.mainFolder:
            if os.path.isdir(main[1]) == True:
                self.changeDirNoLoop(main[1], os.path.abspath(main[1]))
                i = 0
                while i == 0:
                    if os.path.abspath(".") == self.homeDir:
                        self.visitedFolders = set()
                        i = 1
                    else:
                        self.remoteCloud = self.findType(("dir", "file"), os.path.abspath("."), self.remoteCloud)
                        if len(self.remoteCloud) == 0:
                            self.visitedFolders.add(os.path.abspath("."))
                            os.chdir("..")
                        else:
                            if self.remoteCloud[0][0] == "file":
                                self.Iminwhat = os.path.abspath(".")
                                fileChecker(self.remoteCloud[0][1])
                            else:
                                if len(self.remoteCloud[0][1].split(".")) > 1 or " " and ")" and "(" in self.remoteCloud[0][1] or "current" == self.remoteCloud[0][1]:
                                    self.visitedFolders.add(os.path.abspath(self.remoteCloud[0][1]))
                                else:
                                    try:
                                        self.changeDirNoLoop(self.remoteCloud[0][1], os.path.abspath(self.remoteCloud[0][1]))
                                    except:
                                        self.visitedFolders.add(os.path.abspath(self.remoteCloud[0][1]))
            else: fileChecker(main[1])
        for p in self.dupliFiles:
            if len(self.dupliFiles[p][1].split("\n")) < 2:
                pass
            else:
                self.logger.add(self.dupliFiles[p][1])
        self.endMe()#self.dupliFilesLogger
    # First function of this program, also the most powerful, other functions inherited something from it
    def emptyDirsFinder(self):
        os.chdir(os.path.abspath(self.homeDir))
        self.mainFolder = self.findType(("dir"))  # mainFolder wants just names of dirs of local directory
        for main in self.mainFolder:
            i = 0
            self.changeDirNoLoop(main[1], os.path.abspath(main[1]))
            #self.visitedFolders.add(os.path.abspath(main[1]))
            #os.chdir(main[1])
            while i != 1:
                if os.path.abspath(".") == self.homeDir:
                    i = 1
                else:
                    #print(self.remoteCloud)
                    self.remoteCloud = self.findType(("dir"), os.path.abspath("."), self.remoteCloud)
                    try:
                        if len(os.listdir(".")) == 0:
                            self.logger.add(os.getcwd())
                            #self.emptyDirs.write(os.getcwd()+"\n")
                            os.chdir("..")
                        elif len(self.remoteCloud) == 0:
                            os.chdir("..")
                        else:
                            self.changeDirNoLoop(self.remoteCloud[0][1], os.path.abspath(self.remoteCloud[0][1]))
                    except(PermissionError):
                        self.logger.add(os.getcwd())
                        os.chdir("..")
                        #self.visitedFolders.add(os.path.abspath(self.remoteCloud[0][1]))
                        #os.chdir(self.remoteCloud[0][1])
        self.endMe()#self.emptyDirs
    def endMe(self):
        pass
# If you run this program directly, do this, else don't mind me
if __name__ == "__main__":
    print("You shall not pass!!") # The beginning of everything
