import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re

class ohouse:
    def __init__(self):
        self.root = root
        self.file_name = file_name
        self.file_category_num = file_category_num

    def request_url(self, category_num, page):
        url01 = 'https://ohou.se/store/category?category='
        url02 = str(category_num)
        url03 = '&order=popular&page='
        url04 = str(page)
        url05 = '&per=24'
        url = url01 + url02 + url03 +url04 + url05
        print(url)
        try : 
            all = requests.get(url).json()
            infos = all['productions']
        except Exception as e :
            print('URL 오류')
        return infos

    def item_list_info(self, list_item, infos):
        for i in infos:
            try:
                one_item = {}
                one_item['id'] = i['id']
                one_item['name'] = i['name']
                one_item['brand_name'] = i['brand_name']
                one_item['cost'] = i['cost']
                one_item['selling_cost'] =  i['selling_cost']
                one_item['view_count'] = i['view_count']
                one_item['wish_count'] = i['wish_count']
                one_item['review_count'] = i['review_count']
                one_item['review_avg'] = i['review_avg']
                one_item['use_count'] = i['use_count']
                one_item['card_count'] = i['card_count']
                if len(one_item) == 0 :
                    break
            except Exception as e :
                print('여기가 Error') 
            list_item.append(one_item)
        return list_item, one_item

    def save_file(self, list_item, root, file_name):
        df = pd.DataFrame(list_item)
        df.to_excel(root + '오늘의집_{}.xlsx'.format(file_name))
        print('저장완료')
        return df 

    def main(self):
        root = self.root
        file_name = self.file_name
        category_num = self.file_category_num

        list_item = []
        page = 1
        while True:
            try:
                infos =  self.request_url(category_num, page)
                list_item, one_item = self.item_list_info(list_item, infos)
                page += 1 
                if len(one_item) == 0:
                    break
            except Exception as e :
                print('Error')   
        df = self.save_file(list_item, root, file_name)

if __name__ == "__main__":
    root = 'C:/Users/leevi/Desktop/오늘의집/'
    file_category_num = '1'
    file_name = '가구'
    
    one_category_info = ohouse()
    one_category_info.main()


