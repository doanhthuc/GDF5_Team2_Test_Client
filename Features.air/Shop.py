__author__ = "VyHV"

from airtest.core.api import *
from airtest.core.api import using
using("Content.air")
from Content import *
from Features import *
using("Main.air")
from ExcelUtility import *
using("ConfigReader")
from ConfigReader import ConfigReader

auto_setup(__file__)
fName = "Shop"


def runShop(deviceId):
    try:
        ResetArrRs()
        for fn in getFunctionNeedTest(fName):
            print("Running: " + fn)
            eval(fn)
    except Exception as e:
        WriteLogCrash(e, fName)

def buyItem():
    try:
        pass
    except:
        pass
        
def cheatGold():
    poco(BTN_CHEAT_1).click([0.5, 0.5])
    sleep(0.5)

    poco(FIELD_GOLD_CHEAT).click([0.5, 0.5])
    text("10000")

    poco(FIELD_GEM_CHEAT).click([0.1, 0.5])
    text("10000")

    sleep(0.5)

    poco(BTN_SUBMIT_CHEAT).click([0.5, 0.5])
    