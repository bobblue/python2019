import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def make_request_url(page, keyword):
    url01 = 'https://store.musinsa.com/app/product/search?search_type=1&pre_q=&d_cat_cd=&brand=&rate=&page_kind=search&list_kind=small&sort=pop&page='
    url02 = '&display_cnt=120&sale_goods=&ex_soldout=&color=&popup=&chk_research=&q='
    url03 = '&chk_brand=&price1=&price2=&chk_color=&chk_sale=&chk_soldout='
    url_sum = url01 + page + url02 + keyword + url03
    #print(url_sum)
    return url_sum


def request_url(url_sum):
    try:
        req = requests.get(url_sum)
        html = req.text
        soup_data = BeautifulSoup(html, 'html.parser')
       #print(soup_data)
        print("URL request Success")
    except Exception as e:
        print("Error for URL")

    list_brand = []
    list_product = []
    list_price = []
    list_liked_cnt = []
    list_review_cnt = []
    list_review_star = []
    list_each_url = []
    product_num_list = []

    info = soup_data.select('div.article_info')

    for soup in info:
        # brand = soup.select('p.item_title').text
        brand = soup.find("p", {"class": "item_title"}).text
        list_brand.append(brand)
        # print(list_brand)
        try :
            product = soup.find("p", {"class": "list_info"}).find('a').text
            product = product.replace('\r', '')
            product = product.replace('\n', '')
            product = product.replace('\t', '')
            list_product.append(product)
            # print(list_product)
        except Exception as e:
            list_product.append('정보읎음')

        try :
            price = soup.find("p", {"class": "price"}).text
            price = price.replace("\r", '')
            price = price.replace("\n", '')
            price = price.replace("\t", '')
            list_price.append(price)
            # print(list_price)
        except Exception as e:
            list_price.append('정보읎음')

        try:
            liked_cnt = soup.find("span", {"class": "txt_cnt_like"}).text
            liked_cnt = liked_cnt.replace("\r", '')
            liked_cnt = liked_cnt.replace("\n", '')
            liked_cnt = liked_cnt.replace("\t", '')
            list_liked_cnt.append(liked_cnt)
            # print(list_liked_cnt)
        except Exception as e:
            list_liked_cnt.append('0')

        try:
            cnt = soup.find("p", {"class": "point"}).find("span", {"class": "count"}).text
            list_review_cnt.append(cnt)
        except Exception as e:
            list_review_cnt.append('0')
        # print(list_review_cnt)

        try :
            stars = soup.find("p", {"class": "point"}).find("span")
            star = str(stars)
            p = re.compile('score_[0-9]+')
            review_star = p.findall(star)
            if len(review_star) == 1:
                stars = ''.join(review_star)
                stars_ = stars.replace('score_', '')
                stars_ = int(stars_) * 0.1
                list_review_star.append(stars_)
            else:
                list_review_star.append('0')
            # print(list_review_star)
        except Exception as e:
            list_review_star.append('0')

        try :
            urls = soup.find("p", {"class": "list_info"}).find("a")
            # data = soup.find("div", {"class": "article_info"})
            url = 'https://store.musinsa.com'
            url += urls.get('href')
            list_each_url.append(url)

            p = re.compile('\d+/0$')
            product_num = p.findall(url)
            product_num = product_num[0]
            product_num = product_num.replace('/0', '')
            product_num_list.append(product_num)

            # print(list_each_url)
        except Exception as e:
            list_each_url.append('없음')
            product_num_list.append('없음')

    # print(len(list_brand))
    # print(len(list_product))
    # print(len(list_price))
    # print(len(list_liked_cnt))
    # print(len(list_review_cnt))
    # print(len(list_review_star))

    df = pd.DataFrame(
        data={'brand': list_brand, 'product': list_product, 'price': list_price, 'liked_cnt': list_liked_cnt, \
              'review_cnt': list_review_cnt, 'star': list_review_star, 'url': list_each_url, 'product_num':product_num_list})
    return df


def main():
    keyword = str(input('무신사 크롤러 입니다~ 크롤링할 키워드를 입력하세요 : '))
    list_all = []
    df_all = pd.DataFrame()

    for i in range(1, 100):
        page = str(i)
        url_sum = make_request_url(page, keyword)
        df = request_url(url_sum)
        if len(df) == 0:
            break
        df_all = pd.concat([df_all, df], axis=0)

    df_all.to_excel('C:/Users/leevi/Downloads/무신사_크롤링_%s_v2.xlsx' % (keyword), index=False)
    print('저장 완료! ')


if __name__ == "__main__":
    main()


