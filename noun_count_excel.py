# -*- coding: utf-8 -*-

import pandas as pd
from konlpy.tag import Twitter
from collections import Counter


def noun_count(file_name):
    f = open("C:/Users/leevi/Desktop/%s.txt" % (file_name), 'r', encoding='UTF8')
    text = f.read()
    nlp = Twitter()
    nouns = nlp.nouns(text)
    count = Counter(nouns)


    a = []
    b = []
    for k in count.items():
        a.append(k[0])
        b.append(k[1])

    df1 = pd.DataFrame({'단어': a, '빈도수': b})
    df1 = df1.sort_values(by='빈도수', ascending=False)
    # print(df1)
    df1.to_excel('C:/Users/leevi/Desktop/%s_noun_count.xlsx' %(file_name), index=False)


def main():
    # file_name = ''
    file_name_list = ['test11', 'tset16', 'test21', 'test26', 'test31', 'test36', 'test41', 'test46', 'test51', 'test56', 'test61']
    for file_name in file_name_list:
        noun_count(file_name)
        print('저장완료')


if __name__ == "__main__":
    main()


