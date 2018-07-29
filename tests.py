#!/usr/bin/env python3
# David Omrai, 28.7.2018
from nolder import Nolder
import unittest, os

class checkMyCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    # Easy tests of program functionality
    # Time was passing when I tried to make it work, some problems showed bugs and now I use them to make sure that program won't collaps again
    def giveToCompare(self, where, match):
        master = Nolder()
        whereIam = "/".join(os.path.realpath(__file__).split("/")[0:-1])
        master.logger = set()
        master.filesType = "text"
        if whereIam.split("/")[-1] == "unitTests": master.homeDir = whereIam +"/"+where
        else: master.homeDir = whereIam + "/unitTests/"+where
        if match in {"level3D", "level2D", "level1D"}: master.duplicatesFinder()
        elif match in {"level3ED", "level2ED", "level1ED"}: master.emptyDirsFinder()
        else: master.emptyFilesFinder()
        os.chdir("..")
        file = open(os.getcwd()+"/outcome/{0}.txt".format(match),"r")
        fileProp = file.read().split("|")
        file.close()
        fileProp[-1] = fileProp[-1][0:-1]
        self.assertEqual(master.logger, set(fileProp))
    def test_Level1(self):
        self.giveToCompare("level1", "level1D")
        self.giveToCompare("level1", "level1ED")
        self.giveToCompare("level1", "level1EF")
    def test_Level2(self):
        self.giveToCompare("level2", "level2D")
        self.giveToCompare("level2", "level2ED")
        self.giveToCompare("level2", "level2EF")
    def test_Level3(self):
        self.giveToCompare("level3", "level3D")
        self.giveToCompare("level3", "level3ED")
        self.giveToCompare("level3", "level3EF")
if __name__ == "__main__":
    unittest.main()
