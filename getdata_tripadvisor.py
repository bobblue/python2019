import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from bs4 import BeautifulSoup
import re
import csv
from itertools import count

# url로 각 레스토랑 접속해서 레스토랑 정보에 대해서 하나하나 가지고 오는 코드

def get_restaurant_info(url):
    type = 'portugal'

    try:
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        #print("URL request Success")

    except Exception as e:
        print("Error for URL")

    titles = soup.select('div.ppr_rup > h1.heading_title')
    title = ''

    for title in titles :
        title = title.text
        print(title)

    review_count = soup.select('span.header_rating > div > a > span')

    try :
        review_count = review_count[0].text
        review_count = review_count.replace('건의', '')
        review_count = review_count.replace(',', '')
    except Exception as e:
        review_count = '정보없음'

    address = soup.select('span.format_address > span.street-address')

    try :
        address = address[0].text
    except Exception as e:
        address = '정보없음'

    rank_makaos = soup.select('span.header_popularity > b > span')
    rank_makao = ''
    for i in rank_makaos :
        rank_makao = i.text

    price_range = soup.select('div.rating_and_popularity > span.header_tags ')
    try:
        price_range = price_range[0].text
    except Exception as e:
        price_range = '정보없음'

    review_score = soup.select('span.overallRating')
    try :
        review_score = str(review_score[0].text)
    except Exception as e:
        review_score = '정보없음'

    score = soup.select('div.ui_column > span.ui_bubble_rating')
    score_list = []
    for i in score :
        i = str(i)
        score_ = int(re.findall('\d+', i)[0])
        score_list.append(score_)
    print(score_list)

    try :
        food_score = score_list[0]
    except Exception as e:
        food_score = '정보없음'

    try :
        service_score = score_list[1]
    except Exception as e:
        service_score = '정보없음'
    try :
        price_score = score_list[2]
    except Exception as e:
        price_score = '정보없음'
    try:
        atmosphere_score = score_list[3]
    except Exception as e:
        atmosphere_score = '정보없음'

    df1 = pd.DataFrame({'name': title, 'review_counts':review_count, 'address':address, 'rank_makao':rank_makao, \
                                'price_range':price_range, 'review_all': review_score, 'food': food_score, 'service':service_score, 'price':price_score, 'atmosphere':atmosphere_score}, index=[0])

    return df1


def main():
    url1 = 'https://www.tripadvisor.co.kr'
    data_result = pd.DataFrame()
    data = pd.read_table("C:/Users/leevi/PycharmProjects/get_online_review/data_portugal.csv", sep=',')
    type = 'portugal'

    for j in data['resto_url']:
        url2 = str(j)
        url = url1 + url2
        df1 = get_restaurant_info(url)
        data_result = pd.concat([data_result, df1], axis=0)

    data_result.to_csv('data_restoINFO_%s.csv' % (type), mode='w', encoding='utf-8', index=False)


if __name__ == "__main__" :
    main()

