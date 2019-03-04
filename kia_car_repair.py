# 기아차 영업망 

import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import math
from tqdm import tqdm, trange
from pprint import pprint

info_url = "http://red.kia.com/kr/knet/searchAsaList.do"

headers = {"Accept": "application/json, text/javascript, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "219",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "_fbp=fb.1.1551684408085.1312460829; s_ppn=shopping%20tools%7Cbranch%7Cbranch%20list; s_nr=1551684408552-New; s_vnum=1554044400553%26vn%3D1; s_invisit=true; s_prop23=logged%20out; s_fid=2226EC94F827371B-194CF9FC8B352178; s_cc=true; _ga=GA1.2.2092152138.1551684409; _gid=GA1.2.475015885.1551684409; s_ppvl=shopping%2520tools%257Cbranch%257Cbranch%2520list%2C64%2C64%2C937%2C736%2C937%2C1920%2C1080%2C1%2CL; s_ppv=shopping%2520tools%257Cbranch%257Cbranch%2520list%2C100%2C64%2C1925%2C1920%2C937%2C1920%2C1080%2C1%2CP; s_sq=kiamotors-kr-w%252Ckiamotors-global-w%3D%2526pid%253Dshopping%252520tools%25257Cbranch%25257Cbranch%252520list%2526pidt%253D1%2526oid%253Djavascript%25253Avoid%2525280%252529%25253B%2526ot%253DA; WMONID=QiL99n2i2xO; JSESSIONID=XAvTUMwZ6jikPopWQ0RQrDrkXPn5XjcNhrIh0qSIOZNcl9t2UOi1T5hi3pxzEMIY.a21ic3R3c3AwMV9kb21haW4va21ic3R3c3AwMV9tczE=; _gat=1",
        "Host": "red.kia.com",
        "Origin": "http://red.kia.com",
        "Referer": "http://red.kia.com/kr/view/qnet/asn_prct/qnet_asn_prct_index.do",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"}

data = {"funcobj": "goPage_comm",
        "searchType": "caseBy",
        "schTextType": "all",
        "selectType": "all",
        "currpage": "1",
        "pagesize": "830",
        "selectTypeTemp": "all"}

infos = requests.post(info_url, headers = headers, data = data).json()
info = infos['searchAsaList']

kia_repair_list = []
df = pd.DataFrame()

for i in info :
    try :
        kia_car_info = {}
        kia_car_info['idx'] = i['poiId'] if i['poiId'] != "" else None
        kia_car_info['name'] = i['poiName'] 
        kia_car_info['address'] = i['addr']
        kia_car_info['tel'] = i['telNo']
        kia_car_info['description'] = i['rprTypeNm']     
    except Exception as e :
            print('Error')
            
    kia_repair_list.append(kia_car_info)   
    
df = pd.DataFrame(kia_repair_list) 
df.to_excel("C:/Users/leevi/Desktop/기아차정비망.xlsx")
print('저장완료')