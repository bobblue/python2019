# keyword 검색 결과에 나오는 동영상 이름, url, 재생시간, 유튜버이름을 크롤링 하고 csv로 저장한다 

from selenium import webdriver
from bs4 import BeautifulSoup  # html 소스를 해부하기 위한 뷰숲
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame as df  # dataframe 생성을 위함
import time  # time.sleep을 위함

# 크롤링할 키워드 
keyword = '20대 여자 일상'

driver = webdriver.Chrome("c:/chromedriver")
srt_download_path = "c:/pythondata"

# 크롤링할 페이지 설정(한 페이지에 20개씩임)
num_pagedown = 30
start_subtitle_id = 0

driver.get("https://www.youtube.com/results?sp=EgQQASgBQgQIARIA&search_query=" + keyword)  # 필터: 동영상+자막

print("--- src/crawling/get_subtitle.py START chromedriver ---")

## Youtube_search 최종
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
    dataset = df({'title': title, 'url': link, 'play_time': play_time, 'channel_name': channel,
                  'video_id': [j + 1 for j in range(len(title))]})
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
    dataset = dataset.loc[dataset['title'] != ' ', :]

dataset.to_csv('c:/pythondata/youtube_info_%s.csv'%(keyword), mode = 'w', encoding='utf-8', index= False)

print('--- save dataset as csv file : video meta ---"')

