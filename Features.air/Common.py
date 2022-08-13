
from airtest.core.api import *
from airtest.core.api import using
using("Content.air")
from Content import *
from Features import WriteLogRunning

GameConfig = {
    "TOWER": {
        "CANNON": 0,
        "WIZARD": 1,
        "BOOMERANG": 2,
        "BUNNY": 3,
        "BEAR": 4,
        "GOAT": 5,
        "SNAKE": 6,
        "FIRE": 7,
        "FROZEN": 8,
        "TRAP": 9
    }
}

def cheatFunc(gold, gem, trophy, cardType, cardLevel, quantity):
    # click home tab
    poco(BTN_HOME_TAB).click([0.5, 0.5])
    sleep(0.2)

    # click btn cheat
    poco(BTN_CHEAT_1).click([0.5, 0.5])
    sleep(0.2)

    # cheat gold
    if gold is not None:
        poco(FIELD_GOLD_CHEAT).click([0.5, 0.5])
        text(str(gold))
        sleep(0.2)

    # cheat gem
    if gem is not None:
        poco(FIELD_GEM_CHEAT).click([0.1, 0.5])
        text(str(gem))
        sleep(0.2)

    if trophy is not None:
        poco("trophyCheatInput").click([0.1, 0.5])
        text(str(trophy))
        sleep(0.2)

    if cardType is not None:
        poco("cardIdCheatInput").click([0.5, 0.5])
        text(str(cardType))

        poco("cardQuantityCheatInput").click([0.1, 0.5])
        for i in range(6):
            keyevent("KEYCODE_DEL")
        text(str(quantity))
        sleep(0.5)

        if cardLevel is not None:
            poco("cardLevelCheatInput").click([0.5, 0.5])
            for i in range(6):
                keyevent("KEYCODE_DEL")
            text(str(cardLevel))
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
    sleep(0.5)

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

class TowerConfigUtil:
    @staticmethod
    def readConfigJson(cardTypeId, level):
        print("Level == " + str(level))
        import json
    
        towerConfigFile = open("./Config/Tower.json")
        targetBuffFile = open("./Config/TargetBuff.json")
        towerBuffFile = open("./Config/TowerBuff.json")
        potionConfigFile = open("./Config/Potion.json")

        towerCfg = json.load(towerConfigFile)
        targetBuffCfg = json.load(targetBuffFile)
        towerBuffCfg = json.load(towerBuffFile)
        potionCfg = json.load(potionConfigFile)
        potionCfg = potionCfg["potion"]

        data = {}
        rank = TowerConfigUtil.getRankByLevel(level)

        if cardTypeId == GameConfig["TOWER"]["CANNON"] or cardTypeId == GameConfig["TOWER"]["WIZARD"] or cardTypeId == GameConfig["TOWER"]["BOOMERANG"]:
            state = towerCfg["tower"][str(cardTypeId)]["stat"][str(rank)]
            data["damage"] = str(int(state["damage"]))

            attackSpeed = int(state["attackSpeed"]) / 1000
            if attackSpeed.is_integer():
                attackSpeed = int(attackSpeed)
            data["attackSpeed"] = str(attackSpeed) + "s" # 600 ==> 0.6 ==> 0.6s

            range = float(state["range"])
            if range.is_integer():
                range = int(range)
            data["range"] = str(range)

            data["bulletType"] = TowerConfigUtil.getBulletType(state["bulletRadius"])
        
        if cardTypeId == GameConfig["TOWER"]["BUNNY"]:
            state = towerCfg["tower"][str(cardTypeId)]["stat"][str(rank)]
            data["damage"] = str(int(state["damage"]))

            attackSpeed = int(state["attackSpeed"]) / 1000
            if attackSpeed.is_integer():
                attackSpeed = int(attackSpeed)
            data["attackSpeed"] = str(attackSpeed) + "s" # 600 ==> 0.6 ==> 0.6s

            range = float(state["range"])
            if range.is_integer():
                range = int(range)
            data["range"] = str(range)

            data["bulletType"] = TowerConfigUtil.getBulletType(state["bulletRadius"])

            bulletTargetBuffType = towerCfg["tower"][str(cardTypeId)]["bulletTargetBuffType"]
            slowPercent = abs(float(targetBuffCfg["targetBuff"][str(bulletTargetBuffType)]["effects"][str(rank)][0]["value"]) * 100)
            if slowPercent.is_integer():
                slowPercent = int(slowPercent)
            data["slowPercent"] = str(slowPercent) + "%"
        
        if cardTypeId == GameConfig["TOWER"]["BEAR"]:
            state = towerCfg["tower"][str(cardTypeId)]["stat"][str(rank)]
            data["damage"] = str(int(state["damage"]))

            attackSpeed = int(state["attackSpeed"]) / 1000
            if attackSpeed.is_integer():
                attackSpeed = int(attackSpeed)
            data["attackSpeed"] = str(attackSpeed) + "s" # 600 ==> 0.6 ==> 0.6s

            range = float(state["range"])
            if range.is_integer():
                range = int(range)
            data["range"] = str(range)

            data["bulletType"] = TowerConfigUtil.getBulletType(state["bulletRadius"])

            bulletTargetBuffType = towerCfg["tower"][str(cardTypeId)]["bulletTargetBuffType"]
            frozenTime = abs(float(targetBuffCfg["targetBuff"][str(bulletTargetBuffType)]["duration"][str(rank)]) / 1000)
            if frozenTime.is_integer():
                frozenTime = int(frozenTime)
            data["frozenTime"] = str(frozenTime) + "s"

        if cardTypeId == GameConfig["TOWER"]["GOAT"]:
            state = towerCfg["tower"][str(cardTypeId)]["stat"][str(rank)]
            range = float(state["range"])
            if range.is_integer():
                range = int(range)
            data["range"] = str(range)
            
            towerBuffType = str(towerCfg["tower"][str(cardTypeId)]["auraTowerBuffType"])
            damageUp = str(towerBuffCfg["towerBuff"][towerBuffType]["effects"][str(rank)][0]["value"])
            data["damageUp"] = damageUp

        if cardTypeId == GameConfig["TOWER"]["SNAKE"]:
            state = towerCfg["tower"][str(cardTypeId)]["stat"][str(rank)]
            range = float(state["range"])
            if range.is_integer():
                range = int(range)
            data["range"] = str(range)

            towerBuffType = str(towerCfg["tower"][str(cardTypeId)]["auraTowerBuffType"])
            attackSpeedUp = str(towerBuffCfg["towerBuff"][towerBuffType]["effects"][str(rank)][0]["value"])
            data["attackSpeedUp"] = attackSpeedUp

        
        if cardTypeId == GameConfig["TOWER"]["FIRE"]:
            radius = str(potionCfg["0"]["radius"])
            data["radius"] = radius

            damage = float(potionCfg["0"]["adjust"]["player"]["value"])
            if damage.is_integer():
                damage = int(damage)
            data["damage"] = str(damage)

        if cardTypeId == GameConfig["TOWER"]["FROZEN"]:
            damage = float(potionCfg["1"]["adjust"]["player"]["value"])
            if damage.is_integer():
                damage = int(damage)
            data["frozenTime"] = str(damage) + "s"


        return data


    @staticmethod
    def getBulletType(bulletRadius):
        bulletRadius = float(bulletRadius)
        if (bulletRadius > 0):
            return "area"
        else:
            return "single"
    
    @staticmethod
    def getRankByLevel(level):
        level = int(level)
        if level == 1:
            return 1
        
        if level > 1 and level <= 3:
            return 2

        if level >= 4:
            return 3