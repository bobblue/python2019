import pandas as pd
import re

data = pd.read_excel('C:/Users/leevi/Desktop/����Ʈ_3��/���Ż�/���Ż�_ũ�Ѹ�_����.xlsx')
data.head()

p = re.compile('\d+[,]\d+��$')

new_price = []
for i in data['price'] :
    one_price = p.findall(i)
    try: 
        one = str(one_price[0])
    except:
        one = '��������'
    one = one.replace(',', '')
    one = one.replace('��', '')
    new_price.append(one)
    
data['new_price'] = new_price
data.to_excel('C:/Users/leevi/Desktop/����Ʈ_3��/���Ż�/���Ż�_ũ�Ѹ�_����_��������.xlsx')