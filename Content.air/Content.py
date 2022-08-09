# -*- encoding=utf8 -*-
__author__ = "LinhDNA"

from airtest.core.api import *
from poco.drivers.cocosjs import CocosJsPoco

auto_setup(__file__)
poco = CocosJsPoco()

### Team 2
# =========================== Cheat ===========================
BTN_CHEAT_1 = "cheatBtn"
FIELD_GOLD_CHEAT = "goldCheatInput"
FIELD_GEM_CHEAT = "gemCheatInput"
FIELD_TROPHY_CHEAT = "trophyCheatInput"
FIELD_CARD_ID_CHEAT = "cardIdCheatInput"
FIELD_CARD_LEVEL_CHEAT = "cardLevelCheatInput"
FIELD_CARD_QUANTITY_CHEAT = "cardQuantityCheatInput"
BTN_SUBMIT_CHEAT = "submitBtn"
BTN_CLOSE_CHEAT = "closeBtn"


# =========================== Login ===========================
TXT_FIELD_LOGIN = "TextField_1"
BTN_LOGIN = "Button_1"
BTN_PLAY_BATTLE = "battleBtnBackgroundImg"

# =========================== Shop ===========================
### End Team 2

# =========================== General =========================== 

NOTIFICATION = "NOTIFICATIONS"
BTN_CLOSE = "btnClose"
BTN_OK = "btnOk"
BTN_CANCEL = "btnCancel"
TITLE_GUI = "lbTitle"
TXT_GOLD = "lbGold"
# List payment
PAYMENT = "lvPayment"
# UI nhận quà chung
CONGRATS = "congrats"
NODE_GOLD_VPOINT = "nodeGoldVPoint"
NODE_EVENT_ITEM = "nodeEventItem"
BTN_RECEIVE = "btnReceive"
BTN_BACK = "btnBack"
BTN_EXIT = "btnExit"
NO_NAME = "<no-name>"

HTML_MSG = "htmlMsg"

# =========================== Login ===========================

BTN_GUEST = "btnGuest"
BOX_NAME = "ebLoginUsername"
BOX_PASS = "ebLoginPass"
BTN_LOGINZ = "btnLogin"
BTN_REGISTER = "btnRegister"
TXT_ACC_EXISTS = "Akun sudah ada."
TXT_ACC_INCORRECT = "Nama pengguna/Kata sandi salah,"
BTN_OUT_LOGINZ = "btnBack"
loginFB = Template(r"tpl1609905107210.png", record_pos=(-0.006, -0.104), resolution=(1280, 720))

# =========================== Logout =========================== 

BTN_LOG_OUT = "btnLogout"

# =========================== Lobby =========================== 

BTN_VIP = "spineVip"
BTN_SELECT_TABLE = "spineJoinTable"
BTN_PLAY = "spinePlayNow"
NODE_AVATAR = "avatarPlayer"
AVATAR = "sprite"
BTN_SHOP = "spineShop"
BTN_MAIL = "btnMail"
BTN_RANKING = "btnRanking"
FEATURE_WC = "FeatureWeeklyChallenge"
BTN_DEAL_WC = "events/weekly_challenge/event_wc_join"
FEATURE_DB = "FeatureDailyBonus"
BTN_FEATURE = "btnClick"
BTN_SETTING = "btnSetting"
BTN_TUTORIAL = "btnTut"
TXT_GOLD_LOBBY = "lbGold"

BTN_EVENT_HC = "HCMeterLobby"
IMG_FULL = "imgFull"
TXT_MOVE = "lbMove"

BTN_BUY = "btnBuy"
TXT_CLAIM_WELCOME = "lbClaim"

# =========================== Profile =========================== 

TXT_USER_ID = 'lbID'

# =========================== In Table ===========================

BTN_LEAVE_GAME = "btnExit"
HAND_START = "table_start"
NODE_JACKPOT = "nodeJackpot"

NODE_SCORE = "nodeScore"
TXT_TOP_POINT = "lbText0"
TXT_MIDDLE_POINT = "lbText1"
TXT_BOTTOM_POINT = "lbText2"
TXT_TOTAL_POINT = "lbTextTotal"

EFFECT_WIN = "table_winner_glow"

# =========================== Tutorial =========================== 

BTN_GO = "btnCallBack"
BTN_SKIP = "btnSkip"
IMG_HAND = "hand.png"

# =========================== Support =========================== 

SUPPORT = "SOPORTE" # Text in popup Gold Support
BTN_CLAIM_SUPPORT = "btnGet"
CLAIM_WELCOME_GOLD = "Ok, Sweet !!!"

# =========================== Daily Bonus =========================== 

TXT_DAY_BONUS = "lbDay"
TXT_TIME_REMAIN = "lbTimeRemain"
BTN_CLAIM_BONUS = "fx_btn_collect"
SLOT_DAY = "nodeDay" #imgDay1-7
IMG_TICK = "imgTick"
EFFECT_TODAY = "imgFxLight"
TXT_TODAY = "Today"

# =========================== Event WC =========================== 

# TITLE_GUI = 'lbTitle'
POPUP_WC = "imgTouch"
BTN_ACTION = "spineBtnAction"
BTN_WC_IN_TABLE = 'WCProgressTable'
PROGRESS_IN_TABLE = "lbPercent"

TITLE_WC = "Weekly challenge" 
NODE_DAY = "nodeDay"
TXT_DAY_MISSION = "_lbDay"
IMG_NOT_COMPLETE = "_imgEnd"
IMG_COMPLETE = "_imgTick"
TXT_TOTAL_ITEM = "lbTotalItem"

TXT_DAY_CHALLENGE = "lbDayChallenge"
TXT_MISSION_DETAIL = "lbMissionDetail"
TXT_PROGRESS = "lbProgress"
TXT_ITEM_REWARD = "lbItem"
TXT_GOLD_REWARD = "lbGoldReward"
TXT_ACTION = "lbAction"
ACT_PLAY_NOW = "Play Now"
ACT_CLAIM = "Claim"
TXT_THANK = "lbThankYou"

TITLE_DEAL = "Sweet deals" 
NODE_OFFER = "nodeOffer"
TXT_VPOINT = "lbVpoint"
TXT_BONUS = "lbBonus"
TXT_AVAILABLE = "lbAvailable"
TXT_TIME_LEFT = "lbTimeLeft"
TXT_PRICE = "lbPrice"
NODE_BOUGHT = "nodeBought"

# =========================== Popup Claim Gold =========================== 

BG_REASON = 'bgReason'
TXT_REASON = 'lbReason'
GOOD_LUCK = "Buena suerte" # Text in popup claim reward's new user
BUY_SUCCESS = "Compra existosa"
IMG_GOLD = "imgGold"
# TXT_GOLD = "lbGold"
BTN_CLAIM_REWARD = 'btnClaim'

# =========================== Ranking =========================== 

TXT_CLAIM = "lbtextClaim"
TOP_CONGRAT = "¡Muy Bien! ¡sigues asi!"
GUI_RANKING = "Power hand Ranking"
GUI_END_RANKING = "features/ranking_power/ranking_power_title"
BTN_CONFIRM = "btnConfirm"

# =========================== Offers =========================== 

GUI_OFFER_1ST = "imgTitleBanner"
BTN_BUY = "btnBuy"
BTN_SHOP_NOW = "btnShopNow"

GUI_OFFER_NEW_USER = Template(r"tpl1611715298105.png", record_pos=(0.013, -0.18), resolution=(1600, 720))

# =========================== Shop - VIP =========================== 

GUI_SHOP = "lvShop"
listNodePayment = poco('nodePayment').child('NodeBtnView')
listCategory = poco('lvShop').child("<no-name>").child("BaseUINode")
TXT_CURRENT_GOLD = "lbCurGold"
TXT_OLD_GOLD = "lbOldGold"
HTML_EVENT_ITEM = "htmlEventItem"
HTML_VPOINT = "htmlVPoint"
NODE_BONUS = "nodeBonus"
NODE_1ST_BONUS = "htmlBonusFirstPay"

# =========================== Cheat =========================== 

BTN_CHEAT = 'CheatButton'
BTN_CHEAT_PLAYER = "CheatPlayer"
BTN_CHEAT_2M = "2M"
CHEAT_GOLD = "cheat gold"
BTN_CHEAT_PRIVATE = "Cheat"
BOX_GOLD = 'ebGold'
BTN_SEND_CHEAT = 'btnSendCheatPlayer'
BTN_ADD_BOT = "AddBot" 
TXT_TIME_SERVER = "TimeServer"
BTN_ZACC = "Zacc"
TXT_TC_ID = "___tcId___"
BTN_CHEAT_TC = "TestCase"
TXT_POINT = "cheat point"
BTN_SEND = "Send"

TXT_CHEAT_MOVE = "___move___"
BTN_CHEAT_MOVE = "CheatMove"

# =========================== Event HC =========================== 

TUT_EVENT_HC = "events/home_coming/hc_tut_pointer"
BTN_DEAL_HC = "events/home_coming/hc_icon_offer_1"
BTN_SALE_DEAL_HC = "events/home_coming/hc_icon_offer_2"
TXT_TIME_DEAL_HC = "lbTime"
TXT_MAP = "lbMap"
NODE_GOLD_WIN = "pnReward1"
# TXT_GOLD = "lbGold"

TXT_TOTAL_GOLD = "lbTotalGold"

BTN_HOME_NOW = "btnHomeNow"
TXT_HOME_NOW = "lbHomeNow"

NODE_MOVE = "nodeMove"
# TXT_MOVE = "lbMove"
BTN_MOVE = "btnMove"
ACT_MOVE = "Move"

HC_CELL = [
    "Empty",
    "GoldCell_gold_",
    "GonusMoveCell_move_",
    "XGoldCell_",
    "TeleCell_",
    "GiftCell_",
    "HomeCell_",
    "StartCell_"
]

# Deal
GUI_OFFER_HC = "events/home_coming/hc_offer_1"
GUI_SALE_OFFER_HC = "events/home_coming/hc_offer_2"
NODE_GOLD = "nodeGold"
# TXT_GOLD = "lbGold"
NODE_OFFER = "nodeOffer"
NODE_OFFER_X2 = "nodeX2Offer"
# TXT_MOVE = "lbMove"
NODE_VPOINT = "nodeVPoint"
TXT_VPOINT = "lbVPoint"

TXT_COST = "lbCost"
TXT_TIME_DEAL_REMAIN = "lbDayLeft"

NODE_EVENT_IN_TABLE = "HCMeterTable"
TXT_FULL = "imgFull"
TXT_CUR_POINT = "lbCurPoint"
TXT_MAX_POINT = "lbMaxPoint"

TXT_END_BOARD = "lbText1"
TXT_GOLD_HOME = "lbGoldHome"
TXT_GOLD_WIN = "lbGold"