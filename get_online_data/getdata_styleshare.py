import requests
import time
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from bs4 import BeautifulSoup
import re
import csv
from itertools import count


def get_information(url, keyword):
    try:
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        # print("URL request Success")
    except Exception as e:
        print("Error for URL")

    productname = []
    username = []
    content = []
    like_count = []
    comment_count = []

    try:
        products = soup.select('a.goods-name')
        productname.append(products[0].text)
    except Exception as e:
        productname.append('정보없음')
        print("product 정보없음")

    try:
        usernames = soup.select('a.nickname')
        for i in usernames:
            user = i.text
            username.append(user)
    except Exception as e:
        username.append('정보없음')
        print("username 정보없음")

    try:
        contents = soup.select('div.description-wrapper > p.description')
        for i in contents:
            con = i.text
            con = con.replace('\n', '')
            content.append(con)
    except Exception as e:
        content.append('정보없음')
        print("content 정보없음")

    try:
        likes = soup.select('button.list-of-likes')
        for i in likes:
            like_ = i.text
            like_count.append(like_)
    except Exception as e:
        like_count.append('정보없음')
        print("like_count 정보없음")

    try:
        comments = soup.select('p.comments-count > span.op-count')
        for i in comments:
            comment_ = i.text
            comment_ = comment_.replace('(', '')
            comment_ = comment_.replace(')', '')
            comment_count.append(comment_)
    except Exception as e:
        comment_count.append('정보없음')
        print("comment_count 정보없음")

    df2 = pd.DataFrame({'keyword': keyword, 'product_name': productname, 'username': username, 'content': content, 'like_count': like_count,
                        'comment_count': comment_count, 'url': url})
    return df2


def make_url(page, keyword):
    url_01 = 'https://www.stylesha.re/search/styles?limit=20&keyword='
    url_02 = '&offset='
    url = url_01 + keyword + url_02 + page
    print(url)
    return url


def get_data(url):
    try:
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")
    except Exception as e:
        print("Error for URL")

    url_each = soup.select('a.move-to-fullview')

    result = []
    date_list = []
    for i in url_each:
        each_shop = i.get('href')
        # print(each_shop)
        url_front = 'https://www.stylesha.re'
        reviewpage_url = url_front + each_shop
        result.append(reviewpage_url)
        
    dates = soup.select('p.created-at')
    for i in dates :
        date = i.text
        date_list.append(date)

    df1 = pd.DataFrame({'url': result, 'date':date_list})
    print(len(df1))
    #print(df1)
    return df1


def get_url_dataframe(keyword):
    data_result = pd.DataFrame()
    for i in range(0, 20000):
        page = str(i * 20)
        url = make_url(page, keyword)
        df1 = get_data(url)
        if len(df1) == 0:
            break
        else:
            pass
        data_result = pd.concat([data_result, df1], axis=0)
    #data_result.to_excel('C:/Users/leevi/Downloads/styleshare_{}_URL.xlsx'.format(keyword), index=False)
    #print('ULR 정보 저장 완료')
    data = data_result
    return data


def main():
    keyword_list = ['운동화', '스니커즈', '슬립온', '샌들', '슬리퍼']
    #keyword_list = ['운동화']

    for keyword in keyword_list : 
        data = get_url_dataframe(keyword)
        data_result = pd.DataFrame()
        for url in data['url']:
            try:
                df2 = get_information(url, keyword)
            except Exception as e:
                print("Error for URL")

            data_result = pd.concat([data_result, df2], axis=0)
        data_all = pd.merge(data, data_result)   
        data_all.to_excel('C:/Users/leevi/Downloads/styleshare_{}_RESULT.xlsx'.format(keyword), index=False)
        print('{} RESULT 저장 완료'.format(keyword))


if __name__ == "__main__":
    main()




