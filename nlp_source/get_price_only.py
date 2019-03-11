import pandas as pd
import re

data = pd.read_excel('C:/Users/leevi/Desktop/데상트_3월/무신사/무신사_크롤링_백팩.xlsx')
data.head()

p = re.compile('\d+[,]\d+원$')

new_price = []
for i in data['price'] :
    one_price = p.findall(i)
    try: 
        one = str(one_price[0])
    except:
        one = '정보없음'
    one = one.replace(',', '')
    one = one.replace('원', '')
    new_price.append(one)
    
data['new_price'] = new_price
data.to_excel('C:/Users/leevi/Desktop/데상트_3월/무신사/무신사_크롤링_백팩_가격정제.xlsx')