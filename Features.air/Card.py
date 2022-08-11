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
from Common import closePopup, cheatGold, writeResultWithDescription, str2Bool, cheatQuantityCard
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
    
    battleDeckHolder = poco("battleDeckHolderImg")

    if not battleDeckHolder.exists():
        return
    listCardInDeck = []
    
    for cardType in cardTypeIDs:
        cardNode = battleDeckHolder.child("card_type_" + str(cardType))
        if cardNode.exists():
            listCardInDeck.append(cardType)
    
    listCardNotInDeck = list(set(cardTypeIDs).difference(set(listCardInDeck)))

    
