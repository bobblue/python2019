
# -*- coding: utf-8 -*-

import pandas as pd
from konlpy.tag import Twitter
from collections import Counter
from ckonlpy.tag import Twitter


def noun_count(root, file_name, twitter):
    f = open(root + file_name, 'r', encoding='UTF8')
    text = f.read()
    nouns = twitter.nouns(text)
    count = Counter(nouns)

    a = []
    b = []
    for k in count.items():
        a.append(k[0])
        b.append(k[1])

    df1 = pd.DataFrame({'단어': a, '빈도수': b})
    df1 = df1.sort_values(by='빈도수', ascending=False)
    print(df1)
    df1.to_excel(root + '%s_noun_count.xlsx' %(file_name), index=False)

def add_new_word(root):
    dict_name = 'add_dict_for_backpack.xlsx' # 사전 이름
    add_dict = pd.read_excel(root + dict_name)
    new_word = list(add_dict['new_word'])
    return new_word
    
def main():
    root = 'C:/Users/leevi/Desktop/데상트_3월/' # 파일 root 설정
    file_name_list = ['스타일쉐어_content만.txt'] # 명사 추출할 파일 이름 
    
    twitter = Twitter()
    new_word = add_new_word(root) # 사전 추가 안할 때 주석
    twitter.add_dictionary(new_word, 'Noun') #사전추가 안할 때 주석 
    
    for file_name in file_name_list:
        noun_count(root, file_name, twitter)
        print('nous parsing 저장완료')
        

if __name__ == "__main__":
    main()


