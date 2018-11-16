
# 상품을 여러개 선택할 수 있는 경우 크롤링 코드
# http://www.gsshop.com/deal/deal.gs?dealNo=26991037&kwd=%EC%9A%94%EA%B0%80%EB%B3%B5&gsid=srcheshop-lresult&lseq=396001#ProTabN02
# url 안에 dealNo 가 들어 있을 때 사용

from itertools import count
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# 오리지널 ulr 을 넣어서 deal_number 와 prdcd_number 를 추출한다
def get_numbers(url_origin):
  #  url_origin = 'http://www.gsshop.com/deal/deal.gs?dealNo=31981868&lseq=409019-1&arm=2-U-U&expId=pcBestDeal#ProTabN02'
    req = requests.get(url_origin)
    html = req.text
    soup_origin = BeautifulSoup(html, 'html.parser')
    deal_num = soup_origin.find("meta",  property="og:url")
    deal_num = str(deal_num)
    p = re.compile('dealNo=\d+')
    deal_number = str(p.search(deal_num).group()).replace('dealNo=', '')
    # print(deal_number)

    return deal_number

def find_prdcd_num(url_origin):
    # let's find prdcd numbers!
    req = requests.get(url_origin)
    html = req.text
    soup_origin = BeautifulSoup(html, 'html.parser')
    data = soup_origin.find_all("div", attrs={"data-prdcd": True})

    prdcd_list = []
    for i in data:
        prdcd_num_str = str(i)
        k = re.compile('data-prdcd="\d+')
        prdcd_number = str(k.search(prdcd_num_str).group()).replace('data-prdcd="', '')
        prdcd_list.append(prdcd_number)
    prdcd_list = list(set(prdcd_list))

    return prdcd_list

def get_request_url(deal_number, prdcd_number, page_number):
    url1 = 'http://www.gsshop.com/mi15/knownew/revw/page/revwList.gs?prdid='
    url2 = '&dealFlg=Y&$listing=1&'
    url3 = '$page.number='
    url4 = '&$searchPrdCd='
    url5 = '&contentDisNoYn=N'

    url = url1 + deal_number + url2 + url3 + page_number + url4 + prdcd_number + url5
    print(url)

    try :
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")
        return soup

    except Exception as e:
        print("Error for URL")
        return None

def dataHandling(soup,deal_number):
    df_feed_code = []
    df_review = []
    df_date = []
    df_star = []
    df_product = []
    df_select = []

    # 리뷰 모으기 (리뷰가 한줄만 크롤링 된다! 에러!)
    reviews = soup.select(
        'div.content_wrap'
    )
    for review in reviews:
        review_clean = review.text
        review_clean = review_clean.replace('.','')
        review_clean = review_clean.replace(',', '')
        review_clean = review_clean.replace('\n', '')
        review_clean = review_clean.replace('\r', '')
        review_clean = review_clean.replace('\t', '')
        df_review.append(review_clean)

    # 날짜 모으기

    dates = soup.select(
        'span.date'
    )

    for date in dates:
        date = date.text
        date = date.replace('.', '-')
        df_date.append(date)

    # 평점 모으기
    stars = soup.select(
        'span.rating_star'
    )

    for star in stars:
        star_str = str(star)
        p = re.compile('percent\d+')
        star = str(p.search(star_str).group())
        star_clean = star.replace('percent', '')
        df_star.append(star_clean)

    # 구매한 상품 모으기
    products = soup.select(
        'span.prd'
    )
    for product in products:
        product = product.text
        df_product.append(product)
        p = re.compile('\d+')
        select = p.search(product)
        select = str(select.group())
        df_select.append(select)

    # feed_code 부여하기
    codes = soup.select('span.writer')
    for code in codes:
        code_imsi = str(code.text)
        code_imsi = code_imsi.replace('*', '')
        # print(code_imsi)
        code_sum = 'GSshop' + '%s_' % (deal_number) + code_imsi
        df_feed_code.append(code_sum)

    print(len(df_review), len(df_star), len(df_date), len(df_product))

    if len(df_review) == len(df_star) == len(df_date) == len(df_product):
        pass
    else:
        return None

    # 구매평, 날짜, 평점, 상품을 합하여 하나의 데이터 프레임으로 생성
    df1 = pd.DataFrame({'feed_code': df_feed_code, 'content': df_review, 'date': df_date, 'star': df_star,
                        'product_select': df_product, 'select_number':df_select})
    df1 = df1[['feed_code', 'content', 'date', 'star', 'product_select', 'select_number']]
    return df1, df_date


def main():
    for j in count():
        data_result = pd.DataFrame(columns=('feed_code', 'content', 'date', 'star', 'product_select','select_number'))
        url_imsi = []
        url_origin = (str(input('{0}번째 url을 입력하세요 : '.format(j + 1))))
        prdcd_list = find_prdcd_num(url_origin)
        deal_number = get_numbers(url_origin)

        for p in prdcd_list:
            prdcd_number = str(p)

            for i in range(1, 800):
                page_number = str(i)
                soup = get_request_url(deal_number, prdcd_number, page_number)
                df1, df_date = dataHandling(soup, deal_number)
                data_result = pd.concat([data_result, df1], axis=0)
                if len(df_date) == 0:
                    break

        #       print(data_result)
        data_result.to_csv('요가복_data_GSshop_%s.csv'%(deal_number), mode='w', encoding='utf-8', index=False)
        print('저장 완료')



if __name__ == "__main__":
    main()
