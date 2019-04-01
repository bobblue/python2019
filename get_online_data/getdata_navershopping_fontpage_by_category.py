# 네이버 쇼핑 메인 페이지 정보 가지고 오는 크롤러

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from sqlalchemy import create_engine
import pymysql
from itertools import count

def conn_nice():
    engine = create_engine(encoding='utf-8') # 정보 NEEDED
    conn = engine.connect()
    return conn


def get_brand(df):
    title_list = list(df['product_name'])
    brand = []
    for i in title_list :
        p = re.compile('^[^, ]+')
        result = p.findall(i)
        result = str(result)
        result = result.replace('[\'','')
        result = result.replace('\']','')
        result = result.replace('[]', 'None')
        brand.append(result)

    brand_df = pd.DataFrame({'brand':brand})
    return brand_df

def request_url(category_num, page):
    url01 = 'https://search.shopping.naver.com/search/category.nhn?pagingIndex='
    url02 = str(page)
    url03 = '&pagingSize=40&viewType=list&sort=rel&cat_id=50000'
    url04 = str(category_num)
    url05 = '&frm=NVSHPAG'
    url = url01 + url02 + url03 + url04 + url05
    #print(url)

    try:
        req = requests.post(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        # print("URL request Success")
    except Exception as e:
        print("Error for URL")

    info = soup.select('div.info')
    return info


def get_information(category_name, info):
    list_of_all_info = []
    for i in info:
        product_info = {}

        # 상품 개별 URL
        product_url = i.find('a').get('href')
        product_info['product_url'] = str(product_url)

        # 카테고리 명
        product_info['category'] = str(category_name)

        # 상품이름
        title_ = i.find("a", {"class": "tit"}).get("title")
        title = title_.strip()
        product_info['product_name'] = title if title != [] else None

        # 등록일
        date = i.find('span',{'class':'date'}).text
        date = date.replace('등록일 ', '')
        date = date[0:7]
        product_info['upload_date'] = date

        # 가격
        price = i.find("span", {"class": "price"}).find("span",{"class":"num _price_reload"}).text
        price = price.replace("최저", "")
        price = price.replace("\n", "")
        product_info['price'] = price

        # 쇼핑몰 이름
        #try:
        #    mall_name = i.find("span", {"class": "mall_name"}).text
        #    print(mall_name)
        #except:
        #    mall_name = []
        #product_info["description"] = mall_name

        # 리뷰 수
        try:
            review = i.find("a", {"class": "graph"}).text
            review = review.replace("별점", "")
            review = review.replace("리뷰", "")
        except:
            try:
                review = i.find("span", {"class": "desc"}).text
                review = review.replace("별점", "")
                review = review.replace("리뷰", "")
            except:
                review = ''
        product_info['review_cnt'] = review if review != '' else None

        # 광고 여부
        try:
            ads = i.find("a", {"class": "ad_stk"}).text
        except:
            ads = ''
        product_info['ad'] = ads if ads != '' else None

        # 세부 카테고리
        sub = i.find("span", {"class":"depth"}).text
        sub = sub.replace("\t", '')
        sub = sub.replace("\n", '')
        sub = sub.replace(" ", '')
        product_info['sub_category'] = sub

        # product_number, source_name, key_code, data_for
        product_num = i.find("a",{"class":"jjim _jjim"}).get("data-nv-mid")
        product_info['product_num'] = product_num
        product_info['source_name'] = 'navershopping'
        product_info['key_code'] = 'navershopping' + '_' + str(product_num)
        product_info['data_for'] = '한샘샘플'


        list_of_all_info.append(product_info)

    return list_of_all_info


def main():
    result = []

    for idx, num in enumerate(category_num_list):
        category_name = category_name_list[idx]
        category_num = num
        print(idx)
        print(category_name, category_num)
        for page in range(1, page_max):
            info = request_url(category_num, page)
            list_of_all_info = get_information(category_name, info)
            result.extend(list_of_all_info)
            if len(list_of_all_info) == 0 :
                break


    df = pd.DataFrame(result)
    brand_df = get_brand(df)
    result = pd.concat([df, brand_df], axis=1)
    result = result.drop_duplicates(['key_code'])

    writer = pd.ExcelWriter(root + '네이버쇼핑_프론트_0401.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
    result.to_excel(writer,index=False)
    print('엑셀 파일로 저장 완료! ')

    engine = conn_nice()
    try:
        result.to_sql(name='shoppingmal_info', con=engine, if_exists='append', index=False)  # 원래 있는 db에 넣기~
        print('SQL에 저장 완료')
    except Exception as e:
        print('에러나는 이유')
        print(e)

if __name__ == "__main__":
    root = 'C:/Users/leevi/Downloads/'
    #category_num_list = ['105','108']
    #category_name_list = ['서재사무용가구', '인테리어소품']
    category_num_list = ['100','101', '102', '103', '104', '105', '108']
    category_name_list = ['침실가구','거실가구', '주방가구', '수납가구', '아동주니어가구', '서재사무용가구', '인테리어소품']
    page_max = 101
    main()

