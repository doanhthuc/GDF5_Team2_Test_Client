from Common import *
from ConfigReader import ConfigReader
from ExcelUtility import *
from Features import *
from Content import *
import re
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

    sleep(5)

    # find the card to buy
    gold_in_treasure = None
    gold_quantity = None
    card_type_1 = None
    card_type_2 = None
    card_in_treasure_node_1 = None
    card_in_treasure_node_2 = None
    gold_in_treasure = poco("item_receive_11").offspring("cardQuantityTxt")
    gold_quantity = int(gold_in_treasure.get_text().replace("x", ""))
    print(f"gold_in_treasure: {gold_quantity}")
    for i in range(0, 10):
        slot = poco("item_receive_" + str(i))
        if slot.exists():
            card_type_2 = card_type_1
            card_in_treasure_node_2 = card_in_treasure_node_1
            card_type_1 = i
            card_in_treasure_node_1 = slot

    if card_in_treasure_node_1 is None or card_in_treasure_node_2 is None:
        WriteLogRunning(
            1, "Cac vat pham da duoc mua, khong the tien hanh test", "", False, False)
        return

    card_1_quantity = card_in_treasure_node_1.offspring(
        "cardQuantityTxt").get_text().replace("x", "")
    card_2_quantity = card_in_treasure_node_2.offspring(
        "cardQuantityTxt").get_text().replace("x", "")

    card_1_quantity = int(card_1_quantity)
    card_2_quantity = int(card_2_quantity)

    print(f"card_1_quantity: {card_1_quantity}")
    print(f"card_2_quantity: {card_2_quantity}")

    sleep(2)

    poco("receiveBtn").click([0.5, 0.5])

    sleep(0.5)

    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)
    cardItemInInventory1 = poco("card_type_" + str(card_type_1))
    accumulateTxt1 = cardItemInInventory1.offspring("accumulateTxt").get_text()
    accumulateTxt1 = int(re.sub(r"\/\d*", "", accumulateTxt1))

    if not cardItemInInventory1.exists():
        WriteLogRunning(
            caseId, "cardItemInInventory element khong ton tai", "", False, False)
        return

    cardItemInInventory2 = poco("card_type_" + str(card_type_2))
    accumulateTxt2 = cardItemInInventory2.offspring("accumulateTxt").get_text()
    accumulateTxt2 = int(re.sub(r"\/\d*", "", accumulateTxt2))

    print(f"accumulateTxt1: {accumulateTxt1} cardID 1 : {card_type_1}")
    print(f"accumulateTxt1: {accumulateTxt2} cardID 1 : {card_type_2}")

    if card_1_quantity == accumulateTxt1 and card_2_quantity == accumulateTxt2:
        WriteLogRunning(caseId, description, "", False, True)
    else:
        WriteLogRunning(
            caseId, "Update so luong card sau khi mua khong dung", "", False, False)


def openChestWhenHaveAChestIsOpening(caseId, chestId, description, expectedResult):

    goldCheat = 10000

    INIT_GEM = 10000
    closePopup()

    cheatFunc(goldCheat, INIT_GEM)

    expectedResult = str2Bool(expectedResult)
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    poco("treasureSlotNode" + str(chestId)).click([0.5, 0.5])

    sleep(0.5)

    poco("speedUpBtn").click([0.5, 0.5])

    sleep(2)

    # find the card to buy
    gold_in_treasure = None
    gold_quantity = None
    card_type_1 = None
    card_type_2 = None
    card_in_treasure_node_1 = None
    card_in_treasure_node_2 = None
    gold_in_treasure = poco("item_receive_11").offspring("cardQuantityTxt")
    gold_quantity = int(gold_in_treasure.get_text().replace("x", ""))
    print(f"gold_in_treasure: {gold_quantity}")
    for i in range(0, 10):
        slot = poco("item_receive_" + str(i))
        if slot.exists():
            card_type_2 = card_type_1
            card_in_treasure_node_2 = card_in_treasure_node_1
            card_type_1 = i
            card_in_treasure_node_1 = slot

    if card_in_treasure_node_1 is None or card_in_treasure_node_2 is None:
        WriteLogRunning(
            1, "Cac vat pham da duoc mua, khong the tien hanh test", "", False, False)
        return

    card_1_quantity = card_in_treasure_node_1.offspring(
        "cardQuantityTxt").get_text().replace("x", "")
    card_2_quantity = card_in_treasure_node_2.offspring(
        "cardQuantityTxt").get_text().replace("x", "")

    card_1_quantity = int(card_1_quantity)
    card_2_quantity = int(card_2_quantity)

    sleep(2)

    poco("receiveBtn").click([0.5, 0.5])

    sleep(2)

    poco(BTN_INVENTORY_TAB).click()
    sleep(0.5)
    cardItemInInventory1 = poco("card_type_" + str(card_type_1))
    accumulateTxt1 = cardItemInInventory1.offspring("accumulateTxt").get_text()
    accumulateTxt1 = int(re.sub(r"\/\d*", "", accumulateTxt1))

    if not cardItemInInventory1.exists():
        WriteLogRunning(
            caseId, "cardItemInInventory element khong ton tai", "", False, False)
        return

    cardItemInInventory2 = poco("card_type_" + str(card_type_2))
    accumulateTxt2 = cardItemInInventory2.offspring("accumulateTxt").get_text()
    accumulateTxt2 = int(re.sub(r"\/\d*", "", accumulateTxt2))

    print(f"accumulateTxt1: {accumulateTxt1} cardID 1 : {card_type_1}")
    print(f"accumulateTxt1: {accumulateTxt2} cardID 1 : {card_type_2}")

    if card_1_quantity == accumulateTxt1 and card_2_quantity == accumulateTxt2:
        WriteLogRunning(caseId, description, "", False, True)
    else:
        WriteLogRunning(
            caseId, "Update so luong card sau khi mua khong dung", "", False, False)


def openChestWhenHaveAChestIsNotOpening(caseId, chestId, description, expectedResult):
    expectedResult = str2Bool(expectedResult)
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    poco("treasureSlotNode" + str(chestId)).click([0.5, 0.5])

    sleep(0.5)

    poco("receiveBtn").click([0.5, 0.5])
