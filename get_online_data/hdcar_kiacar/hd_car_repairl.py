# 현대차 정비망

import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import math
from tqdm import tqdm, trange
from pprint import pprint

info_url = "https://www.hyundai.com/wsvc/kr/front/biz/serviceNetwork.list.do"
headers = {"Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "62",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "server-id=3; _sdsat_landing_page=https://www.hyundai.com/kr/ko/purchase-guide/branch|1551670540362; _sdsat_session_count=1; _sdsat_traffic_source=; check=true; AMCVS_F46554D957710F697F000101%40AdobeOrg=1; renderid=rend01; WMONID=55jSOONlVn4; _ga=GA1.2.263157097.1551670541; _gid=GA1.2.1817166856.1551670541; s_cc=true; JSESSIONID=1b1qsc9bej7uel7wf6pthet8z; AMCV_F46554D957710F697F000101%40AdobeOrg=1687686476%7CMCIDTS%7C17960%7CMCMID%7C48721691952646312522933469592726065126%7CMCAAMLH-1552284882%7C11%7CMCAAMB-1552284882%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1551687282s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; _sdsat_lt_pages_viewed=11; _sdsat_pages_viewed=11; _gat_gtag_UA_46360746_1=1; mbox=PC#21db65bcabd54cf589dc23bed4e4fa4f.22_41#1614922177|session#eaea63c2f0dd488e86bd28542e04f9c8#1551684620; s_sq=%5B%5BB%5D%5D",
        "Host": "www.hyundai.com",
        "Origin": "https://www.hyundai.com",
        "Referer": "https://www.hyundai.com/kr/ko/purchase-guide/branch",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"}

df = pd.DataFrame()
hd_repair_list = []
for num in range(1, 140):
    data = {"pageNo" : num,
            "searchWord": "",
            "snGubunListSearch":"", 
            "selectBoxCitySearch": "",
            "selectBoxTownShipSearch":"", 
            "selectBoxCity":"" }

    infos = requests.post(info_url, headers = headers, data = data).json()
    info = infos['data']['result']
    if len(info) == 0 :
        break
        
    for i in info:
        try :
            hd_car_info = {}
            hd_car_info['idx'] = i['asnCd'] if i['asnCd'] != "" else None
            hd_car_info['name'] = i ['asnNm']
            hd_car_info['address'] = i ['pbzAdrSbc']
            hd_car_info['tel'] = i ['repnTn']
            hd_car_info['description'] = i ['apimCeqPlntNm']
        except Exception as e :
            print('Error')

        hd_repair_list.append(hd_car_info)

df = pd.DataFrame(hd_repair_list)
#print(df)
df.to_excel("C:/Users/leevi/Desktop/현대차정비망.xlsx")

print('저장완료')