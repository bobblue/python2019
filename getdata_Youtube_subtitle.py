from selenium import webdriver
from bs4 import BeautifulSoup  # html 소스를 해부하기 위한 뷰숲
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame as df  # dataframe 생성을 위함
import pandas as pd
import chardet  # pandas와 함께
import lxml  # xml 처리 모듈인 lxml
import requests  # 크롤링 하려는 url의 response를 가져오기 위한 requests
import time  # time.sleep을 위함
import csv
import re  # 정규표현식
from urllib.request import urlopen
import sys
import os
import datetime
import sqlite3
import shutil
import sys
import pandas as pd

dataset = pd.read_excel("C:/Users/leevi/Downloads/운동화_URL_ALL.xlsx", encoding='utf-8')

driver = webdriver.Chrome("c:/chromedriver")
srt_download_path = 'c:/pythondata'

# 영상 URL로 downsub 사이트 들어가서 입력
link2 = []
data = []

y = 'http://downsub.com'
for i in range(len(dataset['url'])):
    data = re.sub('https://www.youtube.com/watch\?v\=', '', dataset['url'][i])
    link2.append(y + '/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D' + data)
dataset['downsub_url'] = link2

subtitle_language = []
is_auto_generated = []
subtitle_id_list = []
video_id_list = []
subtitle_filename = []

global download_count
global subtitle_id
download_count = 0
start_subtitle_id = 0
subtitle_id = start_subtitle_id + 1

def download_subtitle(url, srt_filename, srt_download_path=srt_download_path):
    global driver
    driver.get(url)
    time.sleep(3)
    filename = max([srt_download_path + f for f in os.listdir(srt_download_path)])
    filename = filename.split('/')[-1]

    global download_count
    download_count += 1
    if not (download_count) % 10:
        print("--- src/crawling/get_subtitle.py     GET subtitle file {} ---".format(download_count))

    global subtitle_id
    video_id_list.append(row['video_id'])
    subtitle_id_list.append(subtitle_id)
    subtitle_filename.append(filename)
    subtitle_id += 1
    
 for index, row in dataset.iterrows():
    r = requests.get(row['downsub_url'])
    s = BeautifulSoup(r.content, 'html.parser')

    b_list = s.findAll('b')

    lang = []
    for k in range(len(b_list)):
        lang.append(b_list[k].next_sibling)
    del lang[lang.index(' to:'):len(lang)]

    if "\xa0\xa0Korean" in lang:
        down1 = b_list[lang.index("\xa0\xa0Korean")]
        y = 'https://downsub.com'

        a = down1.find_all("a")
        a = re.sub('\[<a href=\"\.', '', str(a))
        a = re.sub('\"\>\&gt\;&gt\;Download\&lt\;\&lt\;</a>\]', '', str(a))
        a = re.sub('amp;', '', str(a))

        subtitle_language.append('korean')
        is_auto_generated.append('false')
        download_subtitle(y + a, str(subtitle_id))
        
    elif "\xa0\xa0Korean (auto-generated)" in lang:
        down3 = b_list[lang.index("\xa0\xa0Korean (auto-generated)")]
        y = 'https://downsub.com'

        a = down3.find_all("a")
        a = re.sub('\[<a href=\"\.', '', str(a))
        a = re.sub('\"\>\&gt\;&gt\;Download\&lt\;\&lt\;</a>\]', '', str(a))
        a = re.sub('amp;', '', str(a))

        subtitle_language.append('korean')
        is_auto_generated.append('true')
        download_subtitle(y + a, str(subtitle_id))
        
srt_df = df({'language': subtitle_language, \
             'is_auto_generated': is_auto_generated, \
             'subtitle_id': subtitle_id_list, \
             'video_id': video_id_list, \
             'filename': subtitle_filename})

