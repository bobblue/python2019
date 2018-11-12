
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url1 = 'http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getProductReviewList&prdNo=1840662246&page='
url2 = '1'
url3 = '&pageTypCd=first&reviewDispYn=Y&isPreview=false&reviewOptDispYn=Y&optSearchBtnAndGraphLayer=Y&reviewBottomBtn=Y&openDetailContents=Y&pageSize=100&isIgnoreAuth=false&lctgrNo=1001397&leafCtgrNo=0&groupProductNo=0&groupFirstViewPrdNo=0&selNo=41580890#this'

url = url1 + url2 + url3

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

df_review = []
df_date = []
df_star = []
df_product = []

#리뷰 모으기
reviews = soup.select(
'p.bbs_summary > span.summ_conts > a'
)

for review in reviews :
    review_ = review.text
    review_clean = review_.replace('\n', '')
    review_clean = review_clean.replace('\r', '')
    review_clean = review_clean.replace('\t', '')
    df_review.append(review_clean)
    print(review_clean)

#날짜 모으기
dates = soup.select(
    'span.date'
)

for date in dates :
    date = date.text
    df_date.append(date)
    print(date)

#평점 모으기
stars = soup.select(
 'div.bbs_top > div.top_l > div > p > span'
)
for star in stars :
    star = star.text
    star_clean = int(re.findall('\d', str(star))[1])
    df_star.append(star_clean)
    print(star_clean)

#구매한 상품 모으기
products = soup.select(
    'div.bbs_cont_wrap > div.bbs_cont > p.option_txt'
)
for product in products :
    product = product.text
    df_product.append(product)
    print(product)

print(len(df_review),len(df_star),len(df_date),len(df_product))


# 구매평, 날짜, 평점, 상품을 합하여 하나의 데이터 프레임으로 생성
df1 = pd.DataFrame({'구매평':df_review, '날짜':df_date, '평점':df_star, '상품':df_product})
df1 = df1[['구매평', '날짜', '평점', '상품']]
print(df1)



