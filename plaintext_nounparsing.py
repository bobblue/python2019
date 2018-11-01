# -*- coding: utf-8 -*-

import pandas as pd
from konlpy.tag import Twitter
from collections import Counter

f = open("C:/Users/leevi/PycharmProjects/naverstore/textfilename.txt",'r',encoding='UTF8')
text = f.read()

nlp = Twitter()
nouns = nlp.nouns(text)
count = Counter(nouns)

a = []
b = []
for k in count.items():
    a.append(k[0])
    b.append(k[1])

df1 = pd.DataFrame({'단어':a, '빈도수':b})
df1 = df1.sort_values(by='빈도수', ascending=False)
print(df1)

df1.to_csv('text_nouns_parsing.csv', mode = 'w', encoding='utf-8', index= False)
