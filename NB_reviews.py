from nltk.classify import NaiveBayesClassifier
import pandas as pd
import re
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# KOSAC사전에서 polarity.csv 파일을 불러온다. ngram.과 max.value 행만 사용하도록 df 내용 수정.

filepath = 'C:/Users/leevi/Desktop/데상트_2월/'
dictname = 'mypolarity_for_reviews'
filename = 'testdata_디스커버리'

df_dic = pd.read_excel("{}/{}.xlsx".format(filepath, dictname))


df = df_dic[df_dic['max.value'].notnull()]
df = df[['ngram','max.value']]

# 한글과 영문이 섞여있는 ngram에서, 가장 앞에 있는 한글단어만 추출하는 정규 표현식
p = r'^[가-힣]+'

# KOSAC으로 부터 긍정(POS), 부정(NEG), 중립(NEU)의 사전을 생성한다
pos_dic = []
neg_dic = []
neu_dic = []

for i, row in df.iterrows():
    if row['max.value'] ==  'POS':
        pos_dic.extend(re.findall(p, row['ngram']))
    elif row['max.value'] ==  'NEG':
        neg_dic.extend(re.findall(p, row['ngram']))
    elif row['max.value'] ==  'NEUT':
        neu_dic.extend(re.findall(p, row['ngram']))

# 중복 단어를 제거하기 위해서 set로 만들었다가 list로 변환시킨다
positive_vocab = list(set(pos_dic)) #총 1830개 단어
negative_vocab = list(set(neg_dic)) #총 1623개 단어
neutral_vocab = list(set(neu_dic)) #총 340개 단어

def word_feats(words):
    return dict((word, True) for word in words)

# 사전의 긍정, 부정, 중립단어를 navie bayes에 학습시킬 준비를 한다
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

# 트레인 데이터셋 생성 완료! naive bayes에 학습 시킨다
train_set = negative_features + positive_features + neutral_features
classifier = NaiveBayesClassifier.train(train_set)

df_dic = pd.read_excel("{}/{}.xlsx".format(filepath, dictname))

df = pd.read_excel("{}/{}.xlsx".format(filepath, filename))
data = df[df['content'].notnull()]
print('총 문장수는 '+ str(len(data)) + '개 입니다')

neg = 0; pos = 0 ;neu = 0;
pos_word = [] ; neg_word = [] ;neu_word = [];

# for문으로 예측하고 싶은 문장을 돌려서 한 문장씩 예측 시킨다
for sentence in data['content']:
    sentence = sentence.lower()
    words = sentence.split(',')

    for word in words:
        classResult = classifier.classify(word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
            neg_word.append(word)
            df1 = pd.DataFrame({'content':neg_word, 'NB':'부정'}, columns=['content', 'NB'])
        elif classResult == 'pos':
            pos = pos + 1
            pos_word.append(word)
            df2 = pd.DataFrame({'content':pos_word, 'NB':'긍정'}, columns=['content', 'NB'])
        elif classResult == 'neu' :
            neu = neu +1
            neu_word.append(word)
            #df3 = pd.DataFrame({'content':neu_word, 'NB':'중립'}, columns=['content', 'NB'])

# 결과 출력시키기
print('긍정의 문장 수는 ' + str(pos) +'개 입니다')
print('부정의 문장 수는 ' + str(neg) +'개 입니다')
print('중립의 문장 수는 ' + str(neu) +'개 입니다')

print('긍정인 반응은 ' + str(float(pos)*100 / len(data['content'])) + '% 입니다')
print('부정인 반응은 ' + str(float(neg)*100 /  len(data['content'])) + '% 입니다')
print('중립인 반응은 ' + str(float(neu)*100 /  len(data['content'])) + '% 입니다')

result = pd.concat([df1,df2], axis=0)
result.to_excel("{}/result_{}.xlsx".format(filepath, filename))

