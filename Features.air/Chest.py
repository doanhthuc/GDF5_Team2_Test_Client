from Common import closePopup, cheatGold, writeResultWithDescription, str2Bool
from ConfigReader import ConfigReader
from ExcelUtility import *
from Features import *
from Content import *
__author__ = "ThucPD"


from airtest.core.api import *
from airtest.core.api import using
using("Content.air")
using("Main.air")
using("ConfigReader")

auto_setup(__file__)
fName = "Chest"


def runChest(deviceId):
    try:
        ResetArrRs()
        for fn in getFunctionNeedTest(fName):
            print("Running: " + fn)
            eval(fn)
    except Exception as e:
        WriteLogCrash(e, fName)


def claimChest(caseId, chestId, description, expectedResult):
    expectedResult = str2Bool(expectedResult)
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    poco("treasureSlotNode" + str(chestId)).click([0.5, 0.5])

    sleep(0.5)

    poco("openTreasureBtn").click([0.5, 0.5])

    sleep(2)

    poco("receiveBtn").click([0.5, 0.5])

    sleep(0.5)

    if poco("emptySlotTxt").exits():
        writeResultWithDescription(caseId, description, True, expectedResult)
    else:
        writeResultWithDescription(caseId, description, False, expectedResult)


def openChestWhenHaveAChestIsOpening(caseId, chestId, description, expectedResult):
    expectedResult = str2Bool(expectedResult)
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    poco("treasureSlotNode" + str(chestId)).click([0.5, 0.5])

    sleep(0.5)

    poco("speedUpBtn").click([0.5, 0.5])

    sleep(2)

    poco("receiveBtn").click([0.5, 0.5])

    if poco("emptySlotTxt").exits():
        writeResultWithDescription(caseId, description, True, expectedResult)
    else:
        writeResultWithDescription(caseId, description, False, expectedResult)

def openChestWhenHaveAChestIsNotOpening(caseId, chestId, description, expectedResult):
    expectedResult = str2Bool(expectedResult)
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    poco("treasureSlotNode" + str(chestId)).click([0.5, 0.5])

    sleep(0.5)

    poco("receiveBtn").click([0.5, 0.5])

    if poco("emptySlotTxt").exits():
        writeResultWithDescription(caseId, description, True, expectedResult)
    else:
        writeResultWithDescription(caseId, description, False, expectedResult)