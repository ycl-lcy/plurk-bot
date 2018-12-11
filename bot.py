
import sys, random
import oauth2 as oauth
from plurk_oauth import PlurkAPI

key = "bpahuUGTawKW"
secret = "fiXYi9wmXqGNaKierCDdxBgjgxYv9JDv"
token = "QNSuolJtFoRN"
token_secret = "7sInJr0dvzZg21bKcDomhZflQyMNeCfm" 

plurk = PlurkAPI(key, secret)
plurk.authorize(token, token_secret)


plurk.callAPI("/APP/Timeline/plurkAdd", options={"content": str(random.random()), "qualifier": "is", "limited_to": "[14129109, 11613769, 13734980]"})
