import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from itertools import count

def get_dealnumber(url_origin) :
    #url_origin = 'http://imvely.com/product/detail.html?product_no=15773&cate_no=41&display_group=2&crema-product-reviews-2-page=5'
    url_origin = str(url_origin)
    p = re.compile('product_no=\d+')
    deal_number = str(p.search(url_origin).group()).replace('product_no=', '')
    return deal_number

def get_request_url(deal_number, page_number):
    # url = 'http://widgets6.cre.ma/imvely.com/products/reviews?app=0&iframe=1&iframe_id=crema-product-reviews-2&page=3&parent_url=http%3A%2F%2Fimvely.com%2Fproduct%2Fdetail.html%3Fproduct_no%3D15773%26cate_no%3D41%26display_group%3D2&product_code=15773&widget_env=100&widget_id=82'
    url1 = 'http://widgets6.cre.ma/imvely.com/products/reviews?app=0&iframe=1&iframe_id=crema-product-reviews-2&page='
    url2 = '&parent_url=http%3A%2F%2Fimvely.com%2Fproduct%2Fdetail.html%3Fproduct_no%3D'
    url3 = '%26cate_no%3D41%26display_group%3D2&product_code='
    url4 = '&widget_env=100&widget_id=82'
    url = url1 + page_number + url2 + deal_number + url3 + deal_number + url4

    try :
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        print("URL request Success")
        return soup

    except Exception as e:
        print("Error for URL")
        return None

def get_data(soup, deal_number):
    df_feed_code = []
    df_review = []
    df_date = []
    df_star = []
    df_product = []

    # 작성자 이름 가지고 와서 feed_code 생성하기
    codes = soup.select('div.products_reviews_list_review__info_value')

    for code in codes:
        code_imsi = str(code.text)
        code_imsi = code_imsi.replace('*', '')
        # print(code_imsi)
        code_sum = 'imvely' + '%s_' % (deal_number) + code_imsi
        df_feed_code.append(code_sum)

    #리뷰 모으기
    reviews = soup.select(
        #'div.products_reviews_list_review__message > a.js-link-expand > div'
        'div.products_reviews_list_review__message_content'
    )

    for review in reviews :
        review_ = review.text
        review_clean = review_.replace('\n', '')
        review_clean = review_clean.replace('\r', '')
        review_clean = review_clean.replace('\t', '')
        review_clean = review_clean.replace('  ', '')
        df_review.append(review_clean)
        df_date.append('정보없음')

    #평점모으기
    stars = soup.select(
        'div.products_reviews_list_review__score_text_rating'
    )


    for star in stars :
        star = star.text
        star = star.replace('- ', '')
        df_star.append(star)

    products = soup.select(
        'span.review_option__product_option > span.review_option__product_option_value'
    )

    #선택 상품 모으기
    for i, product in enumerate(products) :
        if i % 2 == 0 :
            df_product.append(product.text)

    if len(df_review) == len(df_star) == len(df_date) == len(df_product):
        pass
    else:
        return None

    df1 = pd.DataFrame({'feed_code':df_feed_code,'content':df_review, 'date':df_date, 'star':df_star, 'product_select':df_product})
    df1 = df1[['feed_code','content', 'date', 'star', 'product_select']]
    return df1, df_star

def main():
    for j in count():
        url_origin = str(input('{0}번째 url을 입력하세요 :'.format(j+1)))
        data_result = pd.DataFrame(columns=('feed_code', 'content', 'date', 'star', 'product_select'))
        deal_number = get_dealnumber(url_origin)

        for i in range(1,900):
            page_number = str(i)
            soup = get_request_url(deal_number, page_number)

            try :
                df1, df_star = get_data(soup, deal_number)
            except Exception as e:
                print(i)
                print("번째 df가 비어 있습니다")
                pass

            if len(df_star) == 0:
                break

            data_result = pd.concat([data_result, df1], axis=0)

    data_result.to_csv('Imvely_%s.csv' % (deal_number), mode='w', encoding='utf-8', index=False)
    print('저장 완료')

if __name__ == "__main__" :
    main()

