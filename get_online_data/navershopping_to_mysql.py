import requests
import datetime
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from bs4 import BeautifulSoup
import re
import csv
from itertools import count


def conn_nice():
    engine = create_engine()
    conn = engine.connect()
    return conn


def get_infomation(url_origin, url, deal_number, number):
    try:
        print(url)
        req = requests.post(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")
    except Exception as e:
        print("Error for URL")

    try:
        print(url)
        req2 = requests.get(url_origin)
        html2 = req2.text
        soup2 = BeautifulSoup(html2, 'html.parser')
        print("2 URL request Success")
    except Exception as e:
        print("2 Error for URL")

    # 상품이름
    name = soup2.find('meta', {'property':'og:title'}).get('content')
    name = name.replace(': 네이버쇼핑', '')
    # 브랜드 이름 
    brand_name = soup2.find('div', {'class':'td_tit_box'}).find('span', {'class':'td_dsc'}).find('em', {'class':'txt'}).text

    username = []
    title = []
    content = []
    star = []
    date = []
    source = []
    feed_code = []

    product_name = []
    brand = []

    # 유저이름
    usernames = soup.select('span.info > span.name')
    for j in usernames:
        j = j.text
        username.append(j)
        number += 1
        feed_code.append(deal_number + '_'+ str(number))
        product_name.append(name)
        brand.append(brand_name)

    titles = soup.select('div.atc_area > p.subjcet')
    for j in titles:
        j = j.text
        title.append(j)

    contents = soup.select('div.atc_area > div.atc')
    for j in contents:
        j = j.text
        content.append(j)

    rates = soup.select('span.curr_avg')
    for j in rates:
        j = j.text
        star.append(j)

    dates = soup.select('div.atc_area > div > span.date')
    for j in dates:
        j = j.text
        j = j[0:10]
        j = j.replace('.', '-')
        date.append(j)

    sources = soup.select('span.info > span.path')
    for j in sources:
        j = j.text
        source.append(j)

    if len(username) == len(title) == len(content) == len(star) == len(date) == len(source):
        pass
    else:
        return None

    df1 = pd.DataFrame(
        {'feed_code': feed_code, 'username': username, 'title': title, 'content': content, 'star': star, 'date': date,
         'source': source, 'product_name':product_name, 'brand':brand})

    return df1, date, number


def make_proper_url(url_origin):
    url_origin = str(url_origin)
    p = re.compile('nv_mid=\d+')
    deal_number = str(p.search(url_origin).group()).replace('nv_mid=', '')
    url1 = 'https://search.shopping.naver.com/detail/review_list.nhn?nvMid='
    url_ = url1 + deal_number
    return url_, deal_number


def main():
    data_for = '테스트테스트'

    url_origin = str(input('크롤링할 url을 입력하세요 : '))
    data_result = pd.DataFrame()
    number = 0

    url_, deal_number = make_proper_url(url_origin)
    for i in range(1, 900):
        page_number = i
        url2 = '&reviewSort=accuracy&reviewType=all&ligh=true'
        url = url_ + '&page=' + str(page_number) + url2
        # print(url)
        df1, date, number = get_infomation(url_origin, url, deal_number, number)
        if len(date) == 0:
            print(date)
            break
        data_result = pd.concat([data_result, df1], axis=0)

    now = datetime.datetime.now()
    crawling_date = now.strftime('%Y-%m-%d')
    option = 'null'

    data_result['data_for'] = data_for
    data_result['crawling_date'] = crawling_date
    data_result['option'] = option
    print(data_result)

    #data_result.to_excel('C:/Users/leevi/Downloads/data_navershopping_%s.xlsx' % (deal_number), index=False)
    engine = conn_nice()

    try:
        data_result.to_sql(name = 'online_shop_review', con=engine, if_exists='append', index=False) #원래 있는 db에 넣기~
        print('저장 완료')
    except Exception as e:
        print('에러나는 이유')
        print(e)


if __name__ == "__main__":
    main()


# 인풋 url 예시
# https://search.shopping.naver.com/detail/lite.nhn?nv_mid=16305551550&cat_id=50000837&frm=NVSHATC&query=%EB%A1%B1%ED%8C%A8%EB%94%A9&NaPm=ct%3Djpi0vh6o%7Cci%3D16cf5c2a9b1d1d938964b82a89047a8147865c1d%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D591fcfff5cd985adc10d62a0ebf6ad242a869190




