# keyword 검색 결과 동영상의 세부 정보까지 한번에 csv 저장

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
import datetime
from selenium import webdriver

def get_basic_info(keyword, num_pagedown) : 
    driver = webdriver.Chrome("c:/chromedriver")
    srt_download_path = "c:/pythondata"
    start_subtitle_id = 0
    driver.get("https://www.youtube.com/results?sp=EgQQASgBQgQIARIA&search_query=" + keyword)  # 필터: 동영상+자막
    print("--- src/crawling/get_subtitle.py START chromedriver ---")

    elm = driver.find_element_by_tag_name('html')
    
    for j in range(num_pagedown):
        elm.send_keys(Keys.END)
        time.sleep(3)

    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    ad = soup.select('div.ytd-promoted-video-renderer > h3')  # 광고
    notices = soup.select('div.ytd-video-renderer > h3 > a')
    notices2 = soup.select('ytd-thumbnail-overlay-time-status-renderer')
    notices3 = soup.select('yt-formatted-string.ytd-video-meta-block')
    print("--- src/crawling/get_subtitle.py START get video meta ---")

    title = []
    link = []
    play_time = []
    channel = []

    if ad == []:
        for i in range(len(notices)):
            try:
                y = 'https://www.youtube.com'
                youtube_url = y + notices[i].get('href')
                title.append(notices[i].get('title'))
                link.append(youtube_url)
                play_time.append(notices2[i].find(text=True).replace("\n", "").replace(" ", ""))
                channel.append(notices3[i].find(text=True))
            except:
                None
        dataset = df({'title': title, 'url': link, 'play_time': play_time, 'channel_name': channel,'video_id': [j + 1 for j in range(len(title))]})
    else:
        title.append(' ')
        link.append(' ')
        for i in range(len(notices)):
            try:
                y = 'https://www.youtube.com'
                youtube_url = y + notices[i].get('href')
                if youtube_url in link + ori_url:
                    continue
                title.append(notices[i].get('title'))
                link.append(youtube_url)
                play_time.append(notices2[i].find(text=True).replace("\n", "").replace(" ", ""))
                channel.append(notices3[i].find(text=True))
            except:
                None
        link.pop()
        title.pop()
        dataset = df({'title': title, \
                      'url': link, \
                      'play_time': play_time, \
                      'channel_name': channel, \
                      'video_id': [j + 1 for j in range(len(title))]})
        #dataset = dataset.loc[dataset['title'] != ' ', :]
    print(dataset)
    return dataset

def get_all_info(keyword, dataset) : 
    date = []
    explain = []
    link = []
    like = []
    unlike = []
    subscribe = []
    hit = []

    driver = webdriver.Chrome("c:/chromedriver")
    
    def num_parser(s):
        if re.findall('[0-9]', s) != []:
            num = int(re.sub('[^0-9]', '', s))
        else:
            num = 0
        if '천' in s:
            num *= 1000
        elif '만' in s:
            num *= 10000
        return num

    for i, url in enumerate(dataset['url']):
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        date_soup = soup.select('span.date')
        explain_soup = soup.select('yt-formatted-string.content')
        like_soup = soup.select('a.ytd-toggle-button-renderer')
        unlike_soup = soup.select('a.ytd-toggle-button-renderer')
        subscribe_soup = soup.select('span.yt-formatted-string')
        hit_soup = soup.select('span.yt-view-count-renderer')

        try :
            date.append(date_soup[0].find(text=True).replace('게시일: ', ''))
        except :
            date.append('정보없음')
            
        try :
            explain.append(explain_soup[0].find(text=True).split('\n\n')[0])
        except :
            explain.append('정보없음')
            
        try :
            like.append(num_parser(str(like_soup[0].findAll(text=True)[-1])))
        except :
            like.append('정보없음')
            
        try :
            unlike.append(num_parser(str(unlike_soup[1].findAll(text=True)[-1])))
        except :
            unlike.append('정보없음')
            
        try:
            subscribe.append(num_parser(str(subscribe_soup[0].find(text=True))))
        except :
            subscribe.append('정보없음')
        
        try:
            hit.append(num_parser(str(hit_soup[0].find(text=True).replace('조회수 ', '').replace('회', '').replace(',', ''))))
        except :
            hit.append('정보없음')
            
        try:
            link.append(url)
        except :
            link.append('정보없음')
    
        # 프린트해서 i 찍어보기
        print(i)
        print('번째 영상 크롤링 중')
       

    dataset2 = df({'url': link, \
                   'uploaded_date': date, \
                   'summary': explain, \
                   'like_count': like, \
                   'unlike_count': unlike, \
                   'subscribe_count': subscribe, \
                   'hit_count': hit, \
                   'keyword': keyword, \
                   'created_date': datetime.datetime.now().isoformat()})
    return dataset2


def main():
    
    keyword = '프랑스 영국'
    num_pagedown = 20
    
    dataset = get_basic_info(keyword, num_pagedown)
    dataset2 = get_all_info(keyword, dataset)
    info_dataset = pd.merge(dataset, dataset2, on = 'url')
    info_dataset.to_csv('c:/pythondata/info_dataset_youtube_%s.csv'%(keyword), mode='w', encoding='utf-8', index=False)
    print('--- save dataset as csv file : done! ---"') 

if __name__ == "__main__":
    main()

