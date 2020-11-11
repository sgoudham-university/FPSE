import unittest
from unittest.mock import MagicMock

from python.src.DataSource.ConfigFromFile import ConfigFromFile
from python.src.DataSource.ConfigFromStub import ConfigFromStub
from python.src.DataSource.ReadFileToList import ReadFileToList
from python.src.Display.InputTest import InputTest
from python.src.Display.OutputTest import OutputTest
from python.src.Engine.RockPaperScissors import RockPaperScissors


class RockTest(unittest.TestCase):
    rock = RockPaperScissors()

    def test_determinWinnerRockRock(self):
        result = self.rock.determineWinner(0, 0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequestStub(self):
        self.rock.setConfig(ConfigFromStub())
        result = self.rock.generateGamesListRequest();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_getListOfGamesMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star War:Darth Vadar,Emperor,Luke Skywalker")
        self.rock.property = []
        self.rock.config.getConfig = MagicMock(return_value=propertyData)
        result = self.rock.getListOfGames();
        self.assertEqual(['Rock Paper Scissors', 'Star War'], result)

    def getUserInput(self, inputs):
        userInput = InputTest()
        userInput.inputList = inputs
        return userInput

    def getComputerInputs(self, inputs):
        computerInput = InputTest()
        computerInput.inputList = inputs
        return computerInput

    def testRockVersusRock(self):
        self.rock.setConfig(ConfigFromStub())
        self.rock.userInput = self.getUserInput([0, 0, 4])
        self.rock.computerInput = self.getComputerInputs([0])
        userOutput = OutputTest()
        self.rock.userOutput = userOutput
        self.rock.play()
        result = userOutput.outputlist.pop(-1)
        self.assertEqual(result, "Draw")

    def testReplay(self):
        self.rock.setConfig(ConfigFromFile())
        fileToList = ReadFileToList()
        self.rock.userInput = self.getUserInput(fileToList.getList("userInputLog.csv"))
        self.rock.computerInput = self.getComputerInputs(fileToList.getList("computerInputLog.csv"))
        fileOutput = fileToList.getList("userOutputLog.csv")
        userOutput = OutputTest()
        self.rock.userOutput = userOutput
        self.rock.play()
        self.assertEqual(userOutput.outputlist, fileOutput)

    def testPropertyRockPaperScissior(self):
        self.rock.setConfig(ConfigFromFile())
        self.assertEqual(self.rock.property[1], "Rock Paper Scissors:Rock,Scissors,Paper")

    def testPropertyMoreThanOne(self):
        config = ConfigFromFile()
        propertyData = config.getConfig()
        self.assertTrue(len(propertyData) >= 1)

    def testAtLeastOneGame(self):
        self.assertTrue(len(self.rock.getListOfGames()) >= 1)

    def testAtLeastOneWeaponList(self):
        self.assertTrue(len(self.rock.getWeaponLists()) >= 1)

    def testFirstWeaponListHasThreeWeapons(self):
        self.assertTrue(len(self.rock.getWeaponLists()) >= 1)


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
