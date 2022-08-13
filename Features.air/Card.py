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
from Common import closePopup, cheatFunc, TowerConfigUtil, GameConfig
from Login import LoginAction
import re

auto_setup(__file__)
fName = "Card"


def runCard(deviceId):
    try:
        ResetArrRs()
        for fn in getFunctionNeedTest(fName):
            print("Running: " + fn)
            eval(fn)
    except Exception as e:
        WriteLogCrash(e, fName)
    

cardTypeIDs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def swap2Card(caseId):
    closePopup()
    
    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)

    listCardTypeInDeck = getListCardTypeInDeck()
    listCardNotInDeck = substract2Array(cardTypeIDs, listCardTypeInDeck)
    
    card1TypeId = listCardNotInDeck[0]
    card1 = getInventoryCardNode(card1TypeId)
    
    card2TypeId = listCardTypeInDeck[0]
    card2 = getInventoryCardNode(card2TypeId)
    
    card1.click([0.5, 0.5])
    sleep(0.2)
    poco("selectBtnlNode").click([0.5, 0.5])
    sleep(0.5)
    card2.click([0.5, 0.5])
    
    newlistCardTypeInDeck = getListCardTypeInDeck()
    newListCardNotInDeck = substract2Array(cardTypeIDs, newlistCardTypeInDeck)
    

    if (card1TypeId in newlistCardTypeInDeck) and (card1TypeId not in newListCardNotInDeck) and (card2TypeId in newListCardNotInDeck) and (card2TypeId not in newlistCardTypeInDeck):
        WriteLogRunning(caseId, "Swap 2 card", "", False, True)
    else:
        WriteLogRunning(caseId, "Swap 2 card", "", False, False)

def upgradeAllCard(des):
    if poco("Button_1").exists():
        LoginAction("vyhv")
    for cardTypeUpgrade in GameConfig["TOWER"].values():
        upgradeCard(cardTypeUpgrade)

def upgradeCard(cardTypeUpgrade):
    INIT_FRAGMENT = 10000
    closePopup()

    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)

    cheatFunc(10000000, 10000000, 10, cardTypeUpgrade, 1, INIT_FRAGMENT)

    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)

    cardNode = getInventoryCardNode(cardTypeUpgrade)
    cardNode.click()
    sleep(0.5)

    isPass = True
    for level in range(1, 10):
        dataLevel = TowerConfigUtil.readConfigJson(cardTypeUpgrade, level)
        keyNames = dataLevel.keys()
        for key in keyNames:
            test_txt = poco("card_holder_" + key).offspring("statValueTxt").get_text()
            expected_txt = dataLevel[key]

            log = "test - " + key + " : expectedResult(" + expected_txt + "), test_txt(" + test_txt + ")"
            print(log)
            if expected_txt != test_txt:
                isPass = False
                msg = "Upgrade tower type = {}, ".format(cardTypeUpgrade) + log
                WriteLogRunning(0, msg, "", False, False)
        print("Level  " + str(level))
        print(dataLevel)
        
        upgradeBtn = poco("upgradeBtnNode")
        goldUpgrade = int(upgradeBtn.offspring("goldValueTxt").get_text())
        print("gold upgrade: " + str(goldUpgrade))

        accumulateTxt = cardNode.offspring("accumulateTxt").get_text()
        nextUpgrageFragement = int(re.sub(r"\d*\/", "", accumulateTxt))
        remainFragment = int(re.sub(r"\/\d*", "", accumulateTxt))

        if (INIT_FRAGMENT != remainFragment):
            isPass = False
            msg = "Fragment wrong (logic = {}, ui = {})".format(INIT_FRAGMENT, remainFragment)
            WriteLogRunning(0, msg, "", False, False)
        INIT_FRAGMENT = INIT_FRAGMENT - nextUpgrageFragement
        
        print("nextUpgrageFragement" + str(nextUpgrageFragement))
        print("remainFragment" + str(remainFragment))
    
        levelTxt = cardNode.offspring("levelTxt").get_text()
        print("level = " + levelTxt)
        if levelTxt != ("Level." + str(level)):
            isPass = False
            msg = "Level display wrong (logic = {}, ui = {})".format(level, levelTxt)
            WriteLogRunning(0, msg, "", False, False)

        upgradeBtn.click([0.5, 0.5])
        sleep(2)
        poco("acceptBtn").click([0.5, 0.5])
        sleep(1)

        if isPass:
            WriteLogRunning(0, "Upgrade card type = {}, level = {}".format(cardTypeUpgrade, level), "", False, True)
        isPass = True
    
    sleep(1)
    
def substract2Array(arrA, arrB):
    return list(set(arrA).difference(set(arrB)))

def getListCardTypeInDeck():
    battleDeckHolder = poco("battleDeckHolderImg")

    if not battleDeckHolder.exists():
        return

    arr = []
    
    for cardType in cardTypeIDs:
        cardNode = battleDeckHolder.child("card_type_" + str(cardType))
        if cardNode.exists():
            arr.append(cardType)
            
    return arr
    
def getInventoryCardNode(cardType):
    return poco("card_type_" + str(cardType))







