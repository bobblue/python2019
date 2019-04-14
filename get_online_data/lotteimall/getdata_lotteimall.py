
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from itertools import count

df = pd.DataFrame()

for i in range(1,500):
    page = i

    url01 = 'http://www.lotteimall.com/goods/searchPrGdasInfoList.lotte?goods_no=&std_goods_no=1200344947&hdr_tp_cd=10&rowsPerPage=10&pageIdx='
    url02 = str(page)
    url03 = '&multipageIdx=&gdas_stfd_val=&gdasAvgScore=&totalCnt=&healthfood_yn=&healthfood_disp=&multi=&opt_desc=&size_desc='

    url = url01 + url02 + url03

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    df_review = []
    df_date = []
    df_star = []
    df_product = []

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

    # 상품명 모으기 
    products = soup.select(
        'div.tit_prod > p.tit'
    )
    for product in products :
        product = product.text
        df_product.append(product)

    # 구매평, 날짜, 평점을 합하여 하나의 데이터 프레임으로 생성
    df1 = pd.DataFrame({'구매평':df_review, '날짜':df_date, '평점':df_star, '상풍명':df_product})
    df = pd.concat([df,df1], axis=0)
    #print(df)
    if len(df1) == 0:
        break

df.to_excel('C:/Users/leevi/Downloads/롯데몰_리뷰_저장2.xlsx', index=False)
print('저장완료')






