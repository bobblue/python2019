
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from itertools import count
from selenium import webdriver

driver = webdriver.Chrome('c:/chromedriver')
driver.implicitly_wait(3)
driver.get('http://www.mulawear.com/shop/shopdetail.html?branduid=494603&xcode=012&mcode=001&scode=&type=Y&sort=manual&cur_code=012001&GfDT=am13UQ==&crema-product-reviews-1-page=2')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

df_review = []
df_date = []
df_star = []

print(soup)

#리뷰 모으기
reviews = soup.select(
'div.products_reviews_list_review__message > a > div:nth-child(13'
#'review_7439 > div > div.products_reviews_list_review__lcontents > div.products_reviews_list_review__content.review_content > div.products_reviews_list_review__content_inner.review_content__collapsed > div.products_reviews_list_review__message > a > div:nth-child(1)'
#review_7439 > div > div.products_reviews_list_review__lcontents > div.products_reviews_list_review__content.review_content > div.products_reviews_list_review__content_inner.review_content__collapsed > div.products_reviews_list_review__message > a > div:nth-child(1)
#review_7439 > div > div.products_reviews_list_review__lcontents > div.products_reviews_list_review__content.review_content > div.products_reviews_list_review__content_inner.review_content__collapsed > div.products_reviews_list_review__message > a > div:nth-child(1)
    )

print(reviews)
print('여기')

for review in reviews :
    print(review)
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










