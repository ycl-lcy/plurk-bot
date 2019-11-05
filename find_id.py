from __future__ import print_function 
import sys, re, urlparse
import oauth2 as oauth
from plurk_oauth import PlurkAPI

OAUTH_REQUEST_TOKEN = "https://www.plurk.com/OAuth/request_token"
OAUTH_kCCESS_TOKEN = "https://www.plurk.com/OAuth/access_token"
key = "TYt8Fv77oT5p"
secret = "3lzEavllllxZokBVgaEoBtcJfgZXaG3p"
token="PN9Y6bampFc2"
token_secret="MRlltKMyv8z7QUEzOpmNJdK5ep0sZB56"

plurk = PlurkAPI(key, secret)
plurk.authorize(token, token_secret)
my_Profile = plurk.callAPI("/APP/Profile/getPublicProfile", options={"user_id": sys.argv[1]})
my_id = my_Profile["user_info"]["id"]
print(my_id)
