# -*- coding: utf-8 -*-

import pandas as pd
from konlpy.tag import Twitter
from collections import Counter
from ckonlpy.tag import Twitter
import re

def noun_count(file_name):
    f = open("C:/Users/leevi/Downloads/%s.txt" % (file_name), 'r', encoding='UTF8')
    text_raw = f.read()
    p = re.compile('[a-zA-Z가-힣0-9]+')
    text_list = p.findall(text_raw)
    text = ' '.join(text_list)
    twitter = Twitter()
    twitter.add_dictionary(['스쉐', '오직스쉐', '테크노','셀엔듀라','디스커버리','비글','뉴발','키작녀','코디','데일리','데일리룩','치즈윅', '슈펜','내셔널지오그래픽','코르테즈', '캔버스', '버켄', '어글리', '아쿠아', 'white', 'black', '어글리슈즈', '아쿠아슈즈', '쪼리', '슬리퍼','글라이더', '슬립온', '티허트', '파츠', '스니커즈', '밸크로', '스탬핑', '트위즈', '다이나쿤', 'descent', 'nike', '나이키','아디다스','뉴발란스','아식스','오니츠카타이거','아식스타이거','푸마','휠라','리복','반스','스케쳐스','컨버스','크록스','라코스테','라코스떼','브룩스','써코니','테바','TEVA','킨','KEEN','버켄스탁','슈콤마보니','닥터마틴','츄바스코','수이코크','케즈','Keds','수페르가','슈페르가','데상트','르꼬끄', '르꼬끄스포르티브','엄브로','러닝화','밧슈','샌달','고프코어','벌키','청키'], 'Noun')
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
    df1.to_excel('C:/Users/leevi/Downloads/%s_noun_count.xlsx' %(file_name), index=False)


def main():
    # file_name = ''
    #file_name_list = ['test11', 'test16', 'test21', 'test26', 'test31', 'test36', 'test41', 'test46', 'test51', 'test56', 'test61']
    file_name_list = ['styleshare_bom']
    for file_name in file_name_list:
        noun_count(file_name)
        print('nous parsing 저장완료')


if __name__ == "__main__":
    main()


