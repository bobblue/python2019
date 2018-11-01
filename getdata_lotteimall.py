
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from itertools import count

url = 'http://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=12563006&infw_disp_no_sct_cd=10&infw_disp_no=0&cart_sn=1&slog=80006_1&allViewYn=N'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

df_review = []
df_date = []
df_star = []

정가에 샀으면 반품했겠지만 할인해서 샀으니 득템
#divCustMultiComment > div.area_list_comment > ul > li:nth-child(1) > div.cont > a > span

#리뷰 모으기
reviews = soup.select(
    'div.cont > a > span'
    )
for review in reviews :
    review_ = review.text
    review_clean = review_.replace('\n', '')
    review_clean = review_clean.replace('\r', '')
    df_review.append(review_clean)

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







