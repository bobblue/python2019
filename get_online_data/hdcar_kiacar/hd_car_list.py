# 현대차 영업망 

import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import math
from tqdm import tqdm, trange
from pprint import pprint

info_url = "https://www.hyundai.com/wsvc/kr/core/front/biz/purchaseGuide/carAgencyFind.getAgentList.do"
headers = {"Accept": '*/*',
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": '69',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "server-id=3; _sdsat_landing_page=https://www.hyundai.com/kr/ko/purchase-guide/branch|1551670540362; _sdsat_session_count=1; _sdsat_traffic_source=; check=true; AMCVS_F46554D957710F697F000101%40AdobeOrg=1; renderid=rend01; WMONID=55jSOONlVn4; JSESSIONID=1icf5444hfys7d7rpr0dwx6tx; _ga=GA1.2.263157097.1551670541; _gid=GA1.2.1817166856.1551670541; AMCV_F46554D957710F697F000101%40AdobeOrg=1687686476%7CMCIDTS%7C17960%7CMCMID%7C48721691952646312522933469592726065126%7CMCAAMLH-1552275340%7C11%7CMCAAMB-1552275340%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1551677740s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; s_cc=true; s_sq=%5B%5BB%5D%5D; _sdsat_lt_pages_viewed=6; _sdsat_pages_viewed=6; _gat_gtag_UA_46360746_1=1; mbox=session#21db65bcabd54cf589dc23bed4e4fa4f#1551673717|PC#21db65bcabd54cf589dc23bed4e4fa4f.22_17#1614915342",
            "Host": "www.hyundai.com",
            "Origin": "https://www.hyundai.com",
            "Referer": "https://www.hyundai.com/kr/ko/purchase-guide/branch",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"}

data = {"lat": 37.5635968,
        "lon": 126.98664959999998,
        "pageNo": 1,
        "rowCount": 820,
        "brAgenScd": ""}

infos = requests.post(info_url, headers = headers, data = data).json()
info = infos['data']['list']

hd_car_list = []

for i in info:
    try:
        hd_car_info = {}
        hd_car_info['idx'] = i['brCd'] if i['brCd'] != "" else None
        hd_car_info['name'] = i['brNm'] if i['brNm'] != "" else None
        hd_car_info['address'] = i['brBdnmNmAdr']
        if len(i['brBdnmNmDtlAdr']) > 1 : 
            address_01 = i['brBdnmNmAdr']
            address_02 = i["brBdnmNmDtlAdr"]
            hd_car_info['address'] = str(address_01) + " " + str(address_02) 
        else :
            pass
    except Exception as e:
        print('Error')
        
    hd_car_info['tel'] = i['tn'] if i['tn'] != "" else None
    hd_car_list.append(hd_car_info)

df = pd.DataFrame(hd_car_list)
df.to_excel("C:/Users/leevi/Desktop/현대차영업망.xlsx")
print('저장완료')

