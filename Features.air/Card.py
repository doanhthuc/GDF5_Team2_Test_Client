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
from Common import closePopup, cheatFunc, writeResultWithDescription, str2Bool, cheatQuantityCard
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


def upgradeCard():
    closePopup()
    
    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)

    listCardTypeInDeck = getListCardTypeInDeck()
    cardTypeUpgrade = listCardTypeInDeck[0]
    
    cheatFunc(10000000, 10000000, 10, cardTypeUpgrade, 1, 10000)

    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)

    cardNode = getInventoryCardNode(listCardTypeInDeck[0])
    cardNode.click()
    sleep(0.5)

    poco("upgradeBtnNode").click([0.5, 0.5])
    sleep(2)
    
    poco("acceptBtn").click([0.5, 0.5])
    
    
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
