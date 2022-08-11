
from airtest.core.api import *
from airtest.core.api import using
using("Content.air")
from Content import *
from Features import WriteLogRunning

def cheatGold(gold, gem):
    # click home tab
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    sleep(0.2)

    # click btn cheat
    poco(BTN_CHEAT_1).click([0.5, 0.5])
    sleep(0.2)

    # cheat gold
    poco(FIELD_GOLD_CHEAT).click([0.5, 0.5])
    text(str(gold))

    # cheat gem
    poco(FIELD_GEM_CHEAT).click([0.1, 0.5])
    text(str(gem))
    sleep(0.2)

    # click btn submit
    poco(BTN_SUBMIT_CHEAT).click([0.5, 0.5])

def cheatQuantityCard(cardType, quantity):
    # click home tab
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    sleep(0.2)

    # click btn cheat
    poco(BTN_CHEAT_1).click([0.5, 0.5])
    sleep(0.2)

    # cheat card type
    poco("cardIdCheatInput").click([0.5, 0.5])
    text(str(cardType))

    # cheat card quantity
    poco("cardQuantityCheatInput").click([0.1, 0.5])
    for i in range(6):
        keyevent("KEYCODE_DEL")
    text(str(quantity))
    sleep(0.2)

    # click btn submit
    poco(BTN_SUBMIT_CHEAT).click([0.5, 0.5])

def closePopup():
    closeBtn = poco("BTN_CLOSE_1")
    if closeBtn.exists():
        closeBtn.click()

def writeResultWithDescription(caseId, description, testResult, expectedResult):
    if testResult == expectedResult:
        WriteLogRunning(caseId, description, "", False, True)
    else:
        WriteLogRunning(caseId, description, "", False, False)

def str2Bool(txt):
    return True if txt.lower() == "true" else False