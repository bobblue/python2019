#기아차 영업망 

import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import math
from tqdm import tqdm, trange
from pprint import pprint

url01 = "https://www.kia.com/api/kia_korea/base/br01/branchInfo.selectBranchInfoList?pageNum="
url02 = "&sc.searchKey%5B2%5D=&sc.searchType%5B2%5D=all&sortKey%5B0%5D=typeSort&sortKey%5B1%5D=branchNm&sortType%5B0%5D=A&sortType%5B1%5D=A"

kia_car_list = []
df = pd.DataFrame()

for k in range(1,80):
    page_num = str(k)
    info_url = url01 + page_num + url02

    info_all = requests.get(info_url).json()
    infos = info_all['dataInfo']

    for i in infos :
        try :
            kia_car_info = {}
            kia_car_info['idx'] = i['branchId'] if i['branchId'] != "" else None
            kia_car_info['name'] = i['branchNm'] 
            kia_car_info['address'] = i['addr']
            kia_car_info['tel'] = i['tel']
        except Exception as e :
            print('Error')

        kia_car_list.append(kia_car_info)
    
df = pd.DataFrame(kia_car_list)
#print(df)

df.to_excel("C:/Users/leevi/Desktop/기아차영업망.xlsx")
print('저장완료')