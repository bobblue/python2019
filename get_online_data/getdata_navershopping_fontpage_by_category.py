# 네이버 쇼핑 메인 페이지 정보 가지고 오는 크롤러 

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_brand(df):
    title_list = list(df['title'])
    brand = []
    for i in title_list :
        p = re.compile('^[^, ]+')
        result = p.findall(i)
        result = str(result)
        result = result.replace('[\'','')
        result = result.replace('\']','')
        result = result.replace('[]', 'None')
        brand.append(result)

    brand_df = pd.DataFrame({'brand':brand})
    return brand_df

def request_url(category_num, page):
    url01 = 'https://search.shopping.naver.com/search/category.nhn?pagingIndex='
    url02 = str(page)
    url03 = '&pagingSize=40&viewType=thumb&sort=rel&cat_id=50000'
    url04 = str(category_num)
    url05 = '&frm=NVSHPAG'
    url = url01 + url02 + url03 + url04 + url05
    #print(url)

    try:
        req = requests.post(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        # print("URL request Success")
    except Exception as e:
        print("Error for URL")

    info = soup.select('div.info')
    return info


def get_information(category_name, info):
    list_of_all_info = []
    for i in info:
        try:
            product_info = {}

            # 카테고리 명
            product_info['category'] = str(category_name)

            # 상품이름
            title_ = i.find("a", {"class": "tit"}).get("title")
            title = title_.strip()
            product_info['title'] = title if title != [] else None

            # reload 날짜
            dd = i.find("span", {"class": "price"})
            date = dd.find("span", {"class": "num _price_reload"}).get("data-reload-date")
            product_info['reload_date'] = date

            # 가격
            price = dd.text
            price = price.replace("최저", "")
            price = price.replace("\n", "")
            product_info['price'] = price

            # 쇼핑몰 이름
            try:
                mall_name = i.find("span", {"class": "mall_name"}).text
            except:
                mall_name = []
            product_info["mall_name"] = mall_name if mall_name != [] else None

            # 리뷰 수
            try:
                review = i.find("a", {"class": "graph"}).text
                review = review.replace("리뷰", "")
            except:
                try:
                    review = i.find("span", {"class": "desc"}).text
                    review = review.replace("리뷰", "")
                except:
                    review = ''
            product_info['review'] = review if review != '' else None

            # 광고 여부
            try:
                ads = i.find("a", {"class": "ad_stk"}).text
            except:
                ads = ''
            product_info['ad'] = ads if ads != '' else None

            list_of_all_info.append(product_info)
        except:
            pass

    return list_of_all_info


def main():
    result = []

    for idx, num in enumerate(category_num_list):
        category_name = category_name_list[idx]
        category_num = num
        print(idx)
        print(category_name, category_num)
        for page in range(1, page_max):
            info = request_url(category_num, page)
            list_of_all_info = get_information(category_name, info)
            result.extend(list_of_all_info)
            if len(result) == 0 :
                break
            #print(result)

    df = pd.DataFrame(result)
    brand_df = get_brand(df)
    result = pd.concat([df, brand_df], axis=1)
    result.to_excel(root + '네이버쇼핑_프론트.xlsx', index=False)
    print('저장 완료! ')


if __name__ == "__main__":
    root = 'C:/Users/leevi/Downloads/'
    #category_num_list = ['100', '101']
    #category_name_list = ['침실가구', '거실가구']
    category_num_list = ['100', '101', '102', '103', '104', '105', '108']
    category_name_list = ['침실가구', '거실가구', '주방가구', '수납가구', '아동주니어가구', '서재사무용가구', '인테리어소품']
    page_max = 101
    main()

