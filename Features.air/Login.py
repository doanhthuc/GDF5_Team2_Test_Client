# -*- encoding=utf8 -*-
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
from Common import writeResultWithDescription, str2Bool

auto_setup(__file__)
fName = "Login"

config = ConfigReader()
configUser = config.getConfigByElement(EXTRA_JS, "User")

def runLogin(deviceId):
    try:
        ResetArrRs()
        for fn in getFunctionNeedTest(fName):
            print("Running: " + fn)
            eval(fn)
    except Exception as e:
        WriteLogCrash(e, fName)   
        
# --------------------------------------Login---------------------------------------

# Start game với accName được truyền vào (trên 6 kí tự). 
# Nếu accName chưa có trong list thì sẽ check Register account đó
def StartGame(caseId, accName, expectedResult, description):
    expectedResult = str2Bool(expectedResult)

    LoginAction(accName)

    testResult = True
    if poco(BTN_PLAY_BATTLE).exists():
        testResult = True
    else:
        testResult = False


    writeResultWithDescription(caseId, description, testResult, expectedResult)

def LoginAndLogout(caseId, accName, expectedResult, description):
    expectedResult = str2Bool(expectedResult)

    LoginAction(accName)
    LogoutAction()

    testResult = None
    if poco(BTN_LOGIN).exists() and poco(TXT_FIELD_LOGIN).exists():
        testResult = True
    else:
        testResult = False

    writeResultWithDescription(caseId, description, testResult, expectedResult)

def LoginAction (accName):
    poco(TXT_FIELD_LOGIN).click()

    for i in range(20):
        keyevent("KEYCODE_DEL")
    text(accName)
    sleep(1)

    poco(BTN_LOGIN).click([0.5, 0.5])
    sleep(3)

def LogoutAction ():
    poco("LogoutButton").click([0.5, 0.5])