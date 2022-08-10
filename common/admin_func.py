import requests
import json
#from airtest.core.api import *

HTTP_PROXY = "http://172.28.103.34:3128"
HTTPS_PROXY = "https://172.28.103.34:3128"

# Lấy access token mới mỗi lần dùng tool cheat
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRldiIsImVtYWlsIjoiZGV2IiwiaWF0IjoxNjUyMDg2NjU5LCJleHAiOjE2NTIxNzMwNTl9.AdlLoRI93RVqODp5uHulJOf2r0Is1duVS2q6MDsuneY"
BASE_URL = "http://localhost:3001/api/"

GAME_ID = "domino99"
GAME_MODE = "DEV"

proxyDict = {
    "http": HTTP_PROXY,
    "https": HTTPS_PROXY,
    "ftp": ""
}

header = {
    "content-type": "application/json",
    "sessionKey": ACCESS_TOKEN
}

def api_post_do_function(user_id, function_id, params):
    """"
        Send post function to admin tool back end
    """
#     try:
    url = BASE_URL + "doFunction"
    data = {
        "gameId": GAME_ID,
        "mode": GAME_MODE,
        "user_id": user_id,
        "id": function_id,
        "params": params
    }
    r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
    print("API status: %s" %r.status_code)
    #sleep(1)
    return r.status_code
#     except json.decoder.JSONDecodeError:
#         print('Failed JSON')

def api_get_user_info():
    """"
        Send get to admin tool back end
    """
    url = BASE_URL + "profile/getUserInfo"
    params = {
        "gameId": GAME_ID,
        "mode": GAME_MODE,
    }
    print(url)
    r = requests.get(url, headers=header, params=params)
    print(r.status_code)
    print(r.text)
    res = json.loads(r.text)
    print("API status: %s, Get user info request status: %s" %(r.status_code, res))
    #sleep(1)
    return r.status_code

def api_change_time_server(time_in_milliseconds):
    """"
        Send cheat time server
    """
    url = BASE_URL + "webmin/cheatTime"
    data = {
        "gameId": GAME_ID,
        "mode": GAME_MODE,
        "time": time_in_milliseconds
    }
    r = requests.post(url, data=json.dumps(data), headers=header)
    res = json.loads(r.text)
    print("API status: %s, Change time request status: %s" %(r.status_code, res))
    #sleep(1)
    return r.status_code

def api_get_model(user_id, model_name):
    """"
        Send post modules to admin tool back end
    """
    url = BASE_URL + "player/getModel"
    data = {
        "gameId": GAME_ID,
        "mode": GAME_MODE,
        "user_id": user_id,
        "modelName": model_name
    }
    r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
    res = json.loads(r.text)['modelData']
    model = json.loads(res)
    print("API status: %s, %s: %s" %(r.status_code, model_name, model))
    return model

print("start ----------------------------")
api_get_user_info()
print("end   ----------------------------")

# import datetime
# x = datetime.datetime.now().timestamp() # Timestamp - giây
# y = datetime.datetime.fromtimestamp(x) # Y-m-d h:m:s
# z = y.strftime("%m") # d/m/Y/H/M
# print("%s========%s============%s" %(x,y,z))
# t = datetime.datetime(2021, 1, 1, 13, 11, 12).timestamp() * 1000
# a = api_changeTimeServer(t)

# a = api_postDoFunction("20721798", "CHEAT_PAYMENT_VIP", ["vip.pack_1"])
# a = api_getModel("20721798", "UProfileModel")
# a = api_postDoFunction("20721798", 'CHEAT_SERVER_TIME', ["2021-6-23","15:0:0"])

# start_app("com.zingplay.laviuda")
# sleep(20)