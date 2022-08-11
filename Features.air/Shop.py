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
fName = "Shop"


def runShop(deviceId):
    try:
        ResetArrRs()
        for fn in getFunctionNeedTest(fName):
            print("Running: " + fn)
            eval(fn)
    except Exception as e:
        WriteLogCrash(e, fName)

def buyCard(caseId, goldCheat, description):
    goldCheat = int(goldCheat)
    
    INIT_GEM = 10000
    closePopup()
    
    cheatGold(goldCheat, INIT_GEM)
    
    # click home tab
    poco(BTN_SHOP_TAB).click([0.5, 0.5])
    sleep(0.2)
    
    # find the card to buy
    slot = None
    cardType = None
    for i in range(0, 10):
        slot = poco("item_slot_" + str(i))
        if slot.exists() and not slot.offspring("<no-name>").exists():
            cardType = i
            break
    if slot is None:
        WriteLogRunning(1, "Cac vat pham da duoc mua, khong the tien hanh test", "", False, False)
        return
    
    # cheat quantity of card
    cheatQuantityCard(cardType, 0)

    # buy card
    poco(BTN_SHOP_TAB).click([0.5, 0.5])
    buy_btn = slot.offspring("buy_btn")    
    buy_btn.click()

    # shop popup and then get quantity, price ==> click buy
    buyCardPopup = poco("buyCardPopup")
    if not buyCardPopup.exists():
        WriteLogRunning(caseId, "buyCardPopup element khong ton tai", "", False, False)
        return
   
    quantity = int(buyCardPopup.offspring("quantity").get_text().replace("x", ""))
    goldPrice = int(buyCardPopup.offspring("priceTxt").get_text())
    
    
    buyCardPopup.offspring("buy_btn").click()
    
    # validate
    currentGold = getCurrentGold()

    if goldCheat >= goldPrice and currentGold != (goldCheat - goldPrice):
        WriteLogRunning(caseId, "Cap nhat vang sau khi mua card sai", "", False, False)
        return
    if goldCheat < goldPrice and currentGold == goldCheat:
        WriteLogRunning(caseId, "Khong du vang de mua card", "", False, True)
        return
    
    poco(BTN_INVENTORY_TAB).click()
    cardItemInInventory = poco("card_type_" + str(cardType))
    
    if not cardItemInInventory.exists():
        WriteLogRunning(caseId, "cardItemInInventory element khong ton tai", "", False, False)
        return
    
    accumulateTxt = cardItemInInventory.offspring("accumulateTxt").get_text()
    # convert "60/5" ==> "60"
    accumulateTxt = int(re.sub(r"\/\d*", "", accumulateTxt))
    
    if accumulateTxt == quantity:
        WriteLogRunning(caseId, description, "", False, True)
    else:
        WriteLogRunning(caseId, "Update so luong card sau khi mua khong dung", "", False, True)

    

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

    currentGem = getCurrentGem()
    currentGold = getCurrentGold()

    if (currentGem == (INIT_GEM - gemPrice) and (currentGold == (INIT_GOLD + goldBuy))):
        writeResultWithDescription(caseId, description, True, expectedResult)
    else:
        writeResultWithDescription(caseId, description, False, expectedResult)

def getCurrentGem():
    return int(poco("gemTxt").get_text().replace(".", ""))
def getCurrentGold():
    return int(poco("goldTxt").get_text().replace(".", ""))