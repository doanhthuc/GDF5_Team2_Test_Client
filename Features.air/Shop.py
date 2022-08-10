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
from Common import closePopup, cheatGold, writeResultWithDescription, str2Bool

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

def buyCard():
    closePopup()

    # click home tab
    poco(BTN_SHOP_TAB).click([0.5, 0.5])
    sleep(0.2)


    

def buyGoldByGem(caseId, gold, gem, description, expectedResult):
    INIT_GOLD = int(gold)
    INIT_GEM = int(gem)

    expectedResult = str2Bool(expectedResult)
    
    closePopup()

    cheatGold(INIT_GOLD, INIT_GEM)

    poco(BTN_SHOP_TAB).click([0.5, 0.5])
    poco("shopItemBtn").click([0.5, 0.5])

    goldBuy = int(poco("goldSlotValueTxt").get_text().replace(".", ""))
    gemPrice = int(poco("buy_btn_gold").offspring("priceTxt").get_text().replace(".", ""))
    poco("buy_btn_gold").offspring("unitIconImg").click([0.5, 0.5])
    sleep(1)

    currentGem = int(poco("gemTxt").get_text().replace(".", ""))
    currentGold = int(poco("goldTxt").get_text().replace(".", ""))

    if (currentGem == (INIT_GEM - gemPrice) and (currentGold == (INIT_GOLD + goldBuy))):
        writeResultWithDescription(caseId, description, True, expectedResult)
    else:
        writeResultWithDescription(caseId, description, False, expectedResult)

    
        
