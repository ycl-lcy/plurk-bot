#coding:utf-8

import sys, random
import oauth2 as oauth
from time import sleep
from plurk_oauth import PlurkAPI
import time 
import json


key = "bpahuUGTawKW"
secret = "fiXYi9wmXqGNaKierCDdxBgjgxYv9JDv"
token = "QNSuolJtFoRN"
token_secret = "7sInJr0dvzZg21bKcDomhZflQyMNeCfm" 

key_min = "cQ9Swk4l7LnR"
secret_min = "seFbSi6M6EJh7yo0O3wD6HdEOUOUyxEZ"
token_min = "cFZ7VVAPy9pC"
token_secret_min = "7WJLtHLl4YglrXYKn1xMvA386l4RlMi3"

plurk = PlurkAPI(key, secret)
plurk.authorize(token, token_secret)

plurk_min = PlurkAPI(key_min, secret_min)
plurk_min.authorize(token_min, token_secret_min)

p = plurk.callAPI("/APP/Timeline/plurkAdd", options={"content": str(random.random()), "qualifier": "asks", "limited_to": "[14129109, 11613769, 5993803, 4708688, 14532002, 7863974, 14756394]"})
p_min = plurk_min.callAPI("/APP/Timeline/plurkAdd", options={"content": str(random.random()), "qualifier": "is", "limited_to": "[7915400, 5993803]"})
sleep(1)
a = plurk_min.callAPI("/APP/Timeline/plurkDelete", options={"plurk_id": str(p_min["plurk_id"])})
