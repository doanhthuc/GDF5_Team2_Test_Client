# -*- encoding=utf8 -*-
__author__ = "LinhDNA"

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
def StartGame(caseId, accName):
    poco("TextField_1").click()
    for i in range(10):
        keyevent("KEYCODE_DEL")
    text("hovanvydut")
    sleep(3)
    poco("Button_1").click([0.5, 0.5])
    sleep(3)
    if poco("battleBtnBackgroundImg").exists():
        WriteLogRunning(caseId, "Login Success", "", False, True)
    else:
        WriteLogRunning(caseId, "Login Fail - Account name is too short", "", False, False)

    # sleep(10)
    # Logout(caseId)



def Logout (caseId):
    poco("LogoutButton").click([0.5, 0.5])