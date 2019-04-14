#현대차 영업망 : https://www.hyundai.com/kr/ko/purchase-guide/branch 
#현대차 정비망 : https://www.hyundai.com/kr/ko/customer-service/service-network/service-reservation-search
#기아차 영업망 : https://www.kia.com/kr/shopping-tools/branch/branch-list.html
#기아차 정비망 : http://red.kia.com/kr/view/qnet/asn_prct/qnet_asn_prct_index.do

import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import math
from tqdm import tqdm, trange
from pprint import pprint
    
def make_dataframe(json, root, file_name):
    df = pd.DataFrame(json)
    #df.to_excel(root + file_name)
    print('수집한 데이터는 ' + str(len(df)) + ' 개 지점' )
    print(file_name +' 저장완료')
    print('------------------------------------------')
    
    
def get_informaiton_hd_sales(page_max):
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
            "rowCount": page_max,
            "brAgenScd": ""}

    infos = requests.post(info_url, headers = headers, data = data).json()

    print('수집할 데이터는 '+ str(infos['data']['totalCount']) + ' 개 (이게 전체 데이터 수!) ')
    
    info = infos['data']['list']

    hd_car_list = []

    for i in info:
        try:
            hd_car_info = {}
            hd_car_info['idx'] = i['brCd'] if i['brCd'] != "" else None
            hd_car_info['name'] = i['brNm'] 
            hd_car_info['address'] = i['brBdnmNmAdr']
            if len(i['brBdnmNmDtlAdr']) > 1 : 
                address_01 = i['brBdnmNmAdr']
                address_02 = i["brBdnmNmDtlAdr"]
                hd_car_info['address'] = str(address_01) + " " + str(address_02) 
            else :
                pass
        except Exception as e:
            pass
        
        
        if len(hd_car_info) == 0:
            break
            
        hd_car_info['tel'] = i['tn'] 
        hd_car_list.append(hd_car_info)
    
    return hd_car_list
    
def get_information_hd_repair(page_max):
    hd_repair_list = []
    
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

    for num in range(1, page_max):
        data = {"pageNo" : num,
                "searchWord": "",
                "snGubunListSearch":"", 
                "selectBoxCitySearch": "",
                "selectBoxTownShipSearch":"", 
                "selectBoxCity":"" }

        infos = requests.post(info_url, headers = headers, data = data).json()
        
        if num == 1:
            print('수집할 데이터는 '+ str(infos['data']['totalCount']) + ' 개 (이게 전체 데이터 수!) ')

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
                pass
            hd_repair_list.append(hd_car_info)

    return hd_repair_list

def get_informaiton_kia_sales(page_max):
    url01 = "https://www.kia.com/api/kia_korea/base/br01/branchInfo.selectBranchInfoList?pageNum="
    url02 = "&sc.searchKey%5B2%5D=&sc.searchType%5B2%5D=all&sortKey%5B0%5D=typeSort&sortKey%5B1%5D=branchNm&sortType%5B0%5D=A&sortType%5B1%5D=A"

    kia_car_list = []
    df = pd.DataFrame()

    for k in range(1, page_max):
        page_num = str(k)
        info_url = url01 + page_num + url02
        info_all = requests.get(info_url).json()
        infos = info_all['dataInfo']

        if k == 1:
            print('수집할 데이터는 '+ str(info_all['totalCount']) + ' 개 (이게 전체 데이터 수!) ')

        for i in infos :
            try :
                kia_car_info = {}
                kia_car_info['idx'] = i['branchId'] if i['branchId'] != "" else None
                kia_car_info['name'] = i['branchNm'] 
                kia_car_info['address'] = i['addr']
                kia_car_info['tel'] = i['tel']
            except Exception as e :
                pass

            if len(kia_car_info) == 0:
                break
                
            kia_car_list.append(kia_car_info)
            
    return kia_car_list 

def get_information_kia_repair(page_max):
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
            "pagesize": page_max,
            "selectTypeTemp": "all"}

    infos = requests.post(info_url, headers = headers, data = data).json()
    info = infos['searchAsaList']
    print('수집할 데이터는 '+ str(info[0]['totalCount']) + ' 개 (이게 전체 데이터 수!) ')
    
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
            pass
        
        if len(kia_car_info) == 0 :
            break
        kia_repair_list.append(kia_car_info)   
    
    return kia_repair_list

def main():
    page_max = 1000
    root = "C:/Users/leevi/Desktop/MNsoft/"
    
    file_name01 = "현대차영업망.xlsx"
    file_name02 = "현대차정비망.xlsx"
    file_name03 = "기아차영업망.xlsx" 
    file_name04 = "기아차정비망.xlsx" 

    # 현대차 영업망 
    hd_car_list = get_informaiton_hd_sales(page_max)
    make_dataframe(hd_car_list, root, file_name01)
    
    # 현대차 정비망
    hd_repair_list = get_information_hd_repair(page_max)
    make_dataframe(hd_repair_list, root, file_name02)
    
    # 기아차 영업망
    kia_car_list = get_informaiton_kia_sales(page_max)
    make_dataframe(kia_car_list, root, file_name03)
    
    # 기아차 정비망
    kia_repair_list = get_information_kia_repair(page_max)
    make_dataframe(kia_repair_list, root, file_name04)

if __name__ == "__main__":
    main()

