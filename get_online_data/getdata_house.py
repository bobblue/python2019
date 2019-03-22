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
        self.file_category_name = file_category_name

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

    def item_list_info(self, list_item, infos, category_name):
        for i in infos:
            one_item = {}
            try:
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
                one_item['category_name'] = category_name
                if len(one_item) == 0 :
                    break
            except Exception as e :
                print('여기가 Error') 
            list_item.append(one_item)
            list_num = len(one_item)
        return list_item, list_num

    def save_file(self, list_item, root, file_name):
        df = pd.DataFrame(list_item)
        df.to_excel(root + '오늘의집_{}.xlsx'.format(file_name))
        print('저장완료')
        return df 

    def main(self):
        root = self.root
        file_name = self.file_name
        category_num_list = self.file_category_num
        category_name_list = self.file_category_name
        list_item = []

        for idx, k in enumerate(category_num_list):
            category_num = k
            category_name = category_name_list[idx]
            page = 1
            while True:
                try:
                    infos =  self.request_url(category_num, page)
                    list_num = 0 
                    list_item, list_num = self.item_list_info(list_item, infos, category_name)
                    page += 1 
                    if list_num == 0:
                        break
                except Exception as e :
                    print('Error')   
                    print(e)
                    break
        df = self.save_file(list_item, root, file_name)

if __name__ == "__main__":
    root = 'C:/Users/leevi/Desktop/오늘의집/'
    file_name = '가구'
    file_category_num = ['0_1', '0_2', '0_8', '0_6', '0_5', '0_4', '0_3', '0_0', '0_7']
    file_category_name = ['소파_거실가구', '침실가구','드세스룸','주방가구','학생_서재가구', '수납가구', '테이블', '의자_스툴', '유아동가구']
    
    one_category_info = ohouse()
    one_category_info.main()


