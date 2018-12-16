import sys, random
import oauth2 as oauth
from time import sleep
from plurk_oauth import PlurkAPI
import time 


key = "bpahuUGTawKW"
secret = "fiXYi9wmXqGNaKierCDdxBgjgxYv9JDv"
token = "QNSuolJtFoRN"
token_secret = "7sInJr0dvzZg21bKcDomhZflQyMNeCfm" 

plurk = PlurkAPI(key, secret)
plurk.authorize(token, token_secret)


p = plurk.callAPI("/APP/Timeline/plurkAdd", options={"content": str(random.random()), "qualifier": "is", "limited_to": "[14129109, 11613769, 13734980]"})
sleep(1)
plurk.callAPI("/APP/Timeline/plurkDelete", options={"plurk_id": str(p["plurk_id"])})
print (time.strftime("%Y/%m/%d %H:%M:%S"))
