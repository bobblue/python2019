import requests
import time
from bs4 import BeautifulSoup
import urllib.parse as urlparse
from urllib.parse import unquote
import urllib3
from sqlalchemy.dialects.mysql import pymysql
 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import re
import unicodedata
import datetime
import logging
import logging.handlers

url = 'https://www.seoulstore.com/api/do/searchProducts'


headers = {"authority": "www.seoulstore.com",
    "method": "POST",
    "path": "/api/do/searchProducts",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-length": "80",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "uuid=77787280-3f1b-11e9-be8a-99be918ff0db; RB_PCID=1551772303345652604; cto_lwid=24228142-0e7a-44ad-a95b-abe82f4c702e; RB_GUID=d6ceffc7-5658-4052-9e49-fa892b6da2ce; _fbp=fb.1.1551772304369.1065796632; _ga=GA1.2.1016649659.1551772305; _gid=GA1.2.1688991527.1552352181; wcs_bt=s_2d9af6c410c4:1552358452; RB_SSID=gx5cG2N355",
    "origin": "https://www.seoulstore.com",
    "referer": "https://www.seoulstore.com/search/%EB%B0%B1%ED%8C%A9/products",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"}


data = {"keyword": "백팩",
    "start": 0,
    "count": 1835,
    "method": "searchProducts",
    "accessToken" : "" }

infos = requests.post(url, params = headers, data = data).json()

info_list = []
for i in infos['items']:
    one_item = {}
    product_name = i['descriptions']['name']
    original_price = i['consumerPrice']
    discount_price = i['discountPrice']
    discount_rate = i['discountRate']
    edit_datetime = i['editDatetime']
    search_keywords = i['searchKeywords']
    brand = i['channel']['descriptions']['channelName']
    like_count = i['wishCount']
    one_item['product_name'] = product_name
    one_item['original_price'] = original_price
    one_item['discount_price'] = discount_price
    one_item['discount_rate'] = discount_rate
    one_item['edit_datetime'] = edit_datetime
    one_item['search_keywords'] = search_keywords
    one_item['brand'] =brand
    one_item['like_count'] =like_count
    info_list.append(one_item)
    
df = pd.DataFrame(info_list)
df.to_excel('C:/Users/leevi/Desktop/데상트_3월/seoulstore.xlsx')
print('저장완료')