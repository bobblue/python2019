import pandas as pd
from konlpy.tag import Twitter
from collections import Counter
from ckonlpy.tag import Twitter

root = 'C:/Users/leevi/Desktop/데상트_3월/네이버쇼핑/'
data = pd.read_excel(root + '백팩_브랜드.xlsx')
brand = list(data['brand'])

naver_data = pd.read_excel(root + '네이버쇼핑_프론트_백팩.xlsx')
print(naver_data.head())
len(naver_data)

match = []

for one_title in naver_data['title']:
    imsi = []
    for one_brand in brand :
        if one_brand in one_title:
            imsi.append(one_title)
            imsi.append(one_brand)
        else :
            pass
    match.append(imsi)

print(len(match))
df = pd.DataFrame(match)
df_imsi = df.loc[:, 0:1]
df_imsi.columns = ['title_02', 'brand']

concat_end = pd.concat([naver_data, df_imsi], axis=1)
concat_end.drop('title_02',1)
#df_all = pd.merge(naver_data, df_imsi)

print(len(concat_end))

dd = concat_end.drop('title_02',1)
dd