
import pandas as pd
from konlpy.tag import Komoran
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import DBSCAN
from gensim.models import Word2Vec

data = pd.read_excel("C:/Users/leevi/Documents/카카오톡 받은 파일/롱패딩_온라인쇼핑몰후기_종합.xlsx")

dic = {feed_code: {'content':content, "star":start} for feed_code, content, start in zip(data['feed_code'].values,data['content'].values,data['star'].values)}

komoran = Komoran()

cv_pos = []
cv_neg = []
for key in dic.keys():
    if type(dic[key]['content']) == str :
        dic[key]['morph'] = komoran.morphs(dic[key]['content'])
        if float(dic[key]['star']) >= 3:
            cv_pos.append(dic[key]['morph'])
        else:
            cv_neg.append(dic[key]['morph'])
    else:
        dic[key]['morph'] = None

model = Word2Vec(cv_pos,size=100, window=3,iter=10)

model.most_similar("정말")


