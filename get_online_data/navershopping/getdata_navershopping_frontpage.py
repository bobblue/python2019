# 네이버 쇼핑 메인 페이지 크롤러 만드는 중

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def request_url(keyword,page):
    url01 = 'https://search.shopping.naver.com/search/all.nhn?origQuery='
    url02 = '&pagingIndex='
    url03 = '&pagingSize=40&viewType=thumb&sort=rel&frm=NVSHPAG&query='
    url =url01 + keyword + url02 + str(page) + url03 + keyword

    try:
        req = requests.post(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")
    except Exception as e:
        print("Error for URL")

    info = soup.select('div.info')
    return info

def get_information(info, list_of_all_info):
    for i in info :  
        try:
            # 상품이름
            product_info = {}
            title_ = i.find("a", {"class": "tit"}).get("title")
            title = title_.strip()
            product_info['title'] = title if title != [] else None
            
            # reload 날짜
            dd = i.find("span", {"class": "price"})
            date = dd.find("span", {"class":"num _price_reload"}).get("data-reload-date")
            product_info['reload_date'] = date
            
            # 가격
            price = dd.text
            price = price.replace("최저", "")
            price = price.replace("\n", "")
            product_info['price'] = price    
            
            # 쇼핑몰 이름 
            try:
                mall_name = i.find("span", {"class":"mall_name"}).text 
            except :
                mall_name = []
            product_info["mall_name"] = mall_name if mall_name != [] else None
                
            # 리뷰 수
            try :
                review = i.find("a", {"class":"graph"}).text
                review = review.replace("리뷰", "")
            except :
                try:
                    review = i.find("span", {"class":"desc"}).text
                    review = review.replace("리뷰", "")
                except:
                    review = ''   
            product_info['review'] = review if review != '' else None
            
            # 광고 여부
            try :
                ads = i.find("a", {"class":"ad_stk"}).text
            except :
                ads = ''
            product_info['ad'] = ads if ads != '' else None
        
            list_of_all_info.append(product_info)               
        except:
            pass

    return list_of_all_info

def main():
    list_of_all_info = [] 
    keyword = '백팩'
    root = 'C:/Users/leevi/Downloads/'

    for page in range(1,101)  :
        info = request_url(keyword, page)
        list_of_all_info = get_information(info, list_of_all_info)
        
    df = pd.DataFrame(list_of_all_info)
    df.to_excel( root + '네이버쇼핑_프론트_%s.xlsx' %(keyword), index=False)
    print('저장 완료! ')
    
if __name__ == "__main__":
    main()

            