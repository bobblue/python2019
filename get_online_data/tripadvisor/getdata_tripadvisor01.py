import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from bs4 import BeautifulSoup
import re
from itertools import count

# type이랑, url 바꾸면 레스토랑 이름이랑 개별 url 크롤링 해오는 코드

type = 'portugal'
page_lists = [ '0', 'oa30-', 'oa60-', 'oa90-']
df_all = pd.DataFrame(columns=('type','title', 'resto_url'))

for i in page_lists :
    url = 'https://www.tripadvisor.co.kr/Restaurants-g664891-c10680-%sMacau.html#EATERY_OVERVIEW_BOX' % (i)

    try:
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")

    except Exception as e:
        print("Error for URL")

    food_type = 'portugal'
    title_list = []
    url_list = []

    titles = soup.select(
        'div.ui_column > div.title'
        )

    for title in titles:
        title_ = title.text
        title = title_.replace('\r', '')
        title = title_.replace('\t', '')
        title = title_.replace('\n', '')
        #print(title)
        title_list.append(title)

    resto_urls = soup.select('div.title > a')

    for resto_url in resto_urls:
        resto_url_ = resto_url['href']
        #print(resto_url_)
        url_list.append(resto_url_)

    #print(len(title_list))
    #print(len(url_list))

    df1 = pd.DataFrame({'type': type,'title':title_list, 'resto_url': url_list})
    df_all = pd.concat([df_all, df1], axis =0)

print(df_all)
df_all.to_csv('data_%s.csv' % (type), mode='w', encoding='utf-8', index=False)
print('저장 완료')





