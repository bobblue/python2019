import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def request_url(url):
    try:
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
       # print("URL request Success")
    except Exception as e:
        print("Error for URL")
    return soup

def get_goods_number(soup, page):
    goods = soup.find("input",{"name":"goods_no"})
    p = re.compile('\d+')
    goods_no = p.findall(str(goods))
    goods_no = ''.join(goods_no)

    similar = soup.find("input",{"name":"similar_no"})
    similar_no = p.findall(str(similar))
    similar_no = ''.join(similar_no)

    url01 = 'https://store.musinsa.com/app/reviews/estimate_list/'
    url02 = '/0/'
    url03 = '/'
    url04 = '?similar_no='
    url05 ='&select_similar_no=&is_cache=&sort='
    
    url_all = url01 + goods_no + url02 + page + url03 + similar_no +url04 + similar_no + url05
    return url_all, goods_no

def get_reviews(soup_data, goods_no):
    date_list = []
    title_list = []
    content_list = []
    option_list = []

    soup_date = soup_data.select('span.date')
    for i in soup_date :
        date = i.text
        date_list.append(date)

    soup_content = soup_data.select('div.pContent')
    for i in soup_content : 
       # date = i.find("span",{"class":"date"})
        title = i.find("div",{"class":"tit"}).text
        title = title.replace('\n', '')
        title = title.replace('\t', '')
        title = title.replace('\r', '')
        title_list.append(title)
        
        content = i.find("span",{"class":"content-review"}).text
        content = content.replace('\n', '')
        content = content.replace('\t', '')
        content = content.replace('\r', '')
        content_list.append(content)

    soup_option = soup_data.select('div.content_object')
    for i in soup_option:
        option = i.text
        option = option.replace('\n', '')
        option = option.replace('\t', '')
        option = option.replace('\r', '')
        option_list.append(option)

    df = pd.DataFrame(data= {'product_no': goods_no, 'date':date_list, 'title':title_list, 'content':content_list, 'option':option_list})
    #print(df)
    return df 
    
def main():
    dataset = pd.read_excel("C:/Users/leevi/Desktop/데상트_2월/무신사_크롤링/무신사_크롤링_슬립온.xlsx", encoding='utf-8')
    url_of_goods = dataset['url']
    df_all = pd.DataFrame()

    for one in url_of_goods :
        url = str(one)
        for page in range(1,1000):
            page = str(page)
            try : 
                soup = request_url(url)
                url_all, goods_no = get_goods_number(soup,page)
                soup_data = request_url(url_all)
                df = get_reviews(soup_data, goods_no)
            except Exception as e:
                print('정보없음')
            if len(df) == 0 :
                break
            df_all = pd.concat([df_all, df], axis = 0)
    
    df_all.to_excel('C:/Users/leevi/Desktop/데상트_2월/무신사_크롤링/무신사_크롤링_댓글_슬립온', index=False)
    print('저장 완료! ')

if __name__ == "__main__":
    main()
