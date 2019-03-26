import pandas as pd
import re

data = pd.read_excel('C:/Users/leevi/Desktop/�ѻ�/���̹�����_����Ʈ_����7��_ī�װ�.xlsx')
title_list = list(data['title'])

brand = []

for i in title_list:
    p = re.compile('^[^, ]+ ')
    result_ = p.findall(i) 
    result_ = str(result_)
    result = result_.replace(' ', '')
    result = result.replace('[\'', '')
    result = result.replace('\']', '')
    result = result.replace('[]','None')
    brand.append(result)
    print(result)
    
brand_list = pd.DataFrame({'brand': brand})
result = pd.concat([data, brand_list], axis=1)
result.to_excel('C:/Users/leevi/Desktop/�ѻ�/���̹�����_����Ʈ_����7��_ī�װ�_�귣���߰�.xlsx', index=False)