#품사 태깅 후 빈도 순으로 나열한 DataFrame 

import pandas as pd
from konlpy.tag import Twitter
from collections import Counter
from konlpy.utils import pprint
from ckonlpy.tag import Twitter
import nltk
from nltk import Text

root = 'C:/Users/leevi/Desktop/데상트_3월/_무신사/'
file_name = '무신사_리뷰_18.txt'

f = open(root + file_name, 'r', encoding='UTF8')
text = f.read()

twitter = Twitter()
twitter.add_dictionary({'백팩','가격대비'}, 'Noun')
twitter.add_dictionary({'일하면서'}, 'Adjective')
twitter.add_dictionary({'듭니다'}, 'Verb')

words = []
pos_category = []

for i in df1['word']:
    words.append(i[0])
    pos_category.append(i[1])

df2 = pd.DataFrame({'word': words, 'pos': pos_category, 'count': df1['count']})
df3 = df2.sort_values(by='count', ascending=False)
print(df3)

#twitter.tagset
