# 형태소 분석(명사 추출) 후 데이터를 파일로 저장한다 
import pandas as pd
from konlpy.tag import Twitter
from collections import Counter

f = open("C:/Users/leevi/Downloads/2030_youtube_all.txt",'r',encoding='UTF8')
text = f.read()

nlp = Twitter()
nouns = nlp.nouns(text)
count = Counter(nouns)

a = []
b = []
for k in count.items():
    a.append(k[0])
    b.append(k[1])

df2 = pd.DataFrame({'단어':a, '빈도수':b})
df2 = df2.sort_values(by='빈도수', ascending=False)
print(df2)

df2.to_excel('C:/Users/leevi/Downloads/all_nouns_parsing.xlsx')

