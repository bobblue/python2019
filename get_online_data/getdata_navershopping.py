import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from bs4 import BeautifulSoup
import re
import csv
from itertools import count

def get_infomation(url, deal_number) :
    try :
        req = requests.post(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")
    except Exception as e:
        print("Error for URL")

    username = []
    title = []
    content = []
    rate = []
    date = []
    source = []
    feed_code = []

    usernames = soup.select('span.info > span.name')
    for j in usernames :
        j = j.text
        username.append(j)
        code_sum = 'Navershopping' + '%s_' % (deal_number) + str(j)
        feed_code.append(code_sum)

    titles = soup.select('div.atc_area > p.subjcet')
    for j in titles :
        j = j. text
        title.append(j)

    contents = soup.select('div.atc_area > div.atc')
    for j in contents:
        j = j.text
        content.append(j)

    rates = soup.select('span.curr_avg')
    for j in rates:
        j = j.text
        rate.append(j)

    dates = soup.select('div.atc_area > div > span.date')
    for j in dates:
        j = j.text
        date.append(j)

    sources = soup.select('span.info > span.path')
    for j in sources :
        j = j.text
        source.append(j)

    if len(username) == len(title) == len(content) == len(rate) == len(date) == len(source) :
        pass
    else:
        return None

    df1 =  pd.DataFrame({'feed_code':feed_code,'username':username, 'title':title, 'content':content, 'rate':rate, 'date':date, 'source':source })
    return df1, date

def make_proper_url(url_origin):
    url_origin = str(url_origin)
    p = re.compile('nv_mid=\d+')
    deal_number = str(p.search(url_origin).group()).replace('nv_mid=', '')
    url1 = 'https://search.shopping.naver.com/detail/review_list.nhn?nvMid='
    url_ = url1 + deal_number
    return url_, deal_number

def main():
    url_origin = str(input('크롤링할 url을 입력하세요 : '))
    data_result = pd.DataFrame()

    url_ , deal_number = make_proper_url(url_origin)
    for i in range(1,900):
        page_number = i
        url2 = '&reviewSort=accuracy&reviewType=all&ligh=true'
        url = url_ + '&page=' + str(page_number) + url2
        #print(url)
        df1, date = get_infomation(url, deal_number)
        if len(date) == 0 :
            print(date)
            break
        data_result = pd.concat([data_result, df1], axis=0)

    data_result.to_csv('data_navershopping_%s.csv' % (deal_number), mode='w', encoding='utf-8', index=False)
    print('저장 완료')

if __name__ == "__main__":
    main()


# 인풋 url 예시
# https://search.shopping.naver.com/detail/lite.nhn?nv_mid=16305551550&cat_id=50000837&frm=NVSHATC&query=%EB%A1%B1%ED%8C%A8%EB%94%A9&NaPm=ct%3Djpi0vh6o%7Cci%3D16cf5c2a9b1d1d938964b82a89047a8147865c1d%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D591fcfff5cd985adc10d62a0ebf6ad242a869190




