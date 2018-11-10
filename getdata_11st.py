import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from itertools import count
from selenium import webdriver

driver = webdriver.Chrome('/Users/flynn/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getProductReviewList&prdNo=1840662246&page=3&pageTypCd=first&reviewDispYn=Y&isPreview=false&reviewOptDispYn=Y&optSearchBtnAndGraphLayer=Y&reviewBottomBtn=Y&openDetailContents=Y&pageSize=100&isIgnoreAuth=false&lctgrNo=1001397&leafCtgrNo=0&groupProductNo=0&groupFirstViewPrdNo=0&selNo=41580890#this')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

df_review = []
df_date = []
df_star = []

#리뷰 모으기
reviews = soup.select(
'span.summ_conts > a'
#reviewContTxt
)

for review in reviews :
    review_ = review.text
    review_clean = review_.replace('\n', '')
    review_clean = review_clean.replace('\r', '')
    df_review.append(review_clean)
    print(review_clean)

#날짜 모으기
dates = soup.select(
    'div.info_list > p.numdate'
    )
for date in dates :
    date_ = date.text
    pattern = r'\d+/(\d+)/(\d+)'
    r = re.compile(pattern)
    match = r.search(date_)
    df_date.append(match.group(0))

#평점 모으기
stars = soup.select(
    'div.info_list > div > div'
    )
for star in stars :
    star_clean = int(re.findall('\d', str(star))[0])
    df_star.append(star_clean)

# 구매평, 날짜, 평점을 합하여 하나의 데이터 프레임으로 생성
df1 = pd.DataFrame({'구매평':df_review, '날짜':df_date, '평점':df_star})
df1 = df1[['구매평', '날짜', '평점']]
print(df1)
