import pandas as pd
import re
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import RegexpTokenizer

df = pd.read_excel("C:/Users/leevi/Desktop/데상트_2월/무신사_크롤링/dict_musinsa.xlsx")
df.head()

df_content = pd.read_excel("C:/Users/leevi/Desktop/데상트_2월/무신사_크롤링/봄_댓글전체_python_test.xlsx")
df_content.head()

price = [];price_neg = []; gapoom_neg = []; light = []; season = []; hard_neg = []; daily = []; design = []; size = []
color = []; present =[]; mode =[]; feel=[]; feel_neg=[]; couple = []; quality_neg = []

for i,row in df.iterrows():
    if row['category'] == '사이즈':
        size.append(row['word'])
    elif row['category'] == '가격':
        price.append(row['word'])
    elif row['category'] == '가격-부정':
        price_neg.append(row['word'])
    elif row['category'] == '가품의심-부정':
        gapoom_neg.append(row['word'])
    elif row['category'] == '경량':
        light.append(row['word'])
    elif row['category'] == '계절':
        season.append(row['word'])
    elif row['category'] == '내구성-부정':
        hard_neg.append(row['word'])
    elif row['category'] == '데일리':
        daily.append(row['word'])
    elif row['category'] == '디자인':
        design.append(row['word'])
    elif row['category'] == '색상':
        color.append(row['word'])
    elif row['category'] == '선물':
        present.append(row['word'])
    elif row['category'] == '유행':
        mode.append(row['word'])
    elif row['category'] == '착화감':
        feel.append(row['word'])
    elif row['category'] == '착화감-부정':
        feel_neg.append(row['word'])
    elif row['category'] == '커플':
        couple.append(row['word'])
    elif row['category'] == '품질-부정':
        quality_neg.append(row['word'])

#for sentence in df_content['content'] :
size_c = []; price_c = [];price_neg_c = []; gapoom_neg_c = []; light_c = []; season_c = []; hard_neg_c = []; daily_c = []; design_c = [];
color_c = []; present_c =[]; mode_c =[]; feel_c=[]; feel_neg_c=[]; couple_c = []; quality_neg_c = []

for sentence in df_content['content'] :
    try : 
        words = sentence.split('.')
        #print(words)
        for i in size : 
            size_yes = [s for s in words if i in s] 
            if len(size_yes) > 0 :
                size_c.append(size_yes)
        for i in price : 
            price_yes = [s for s in words if i in s] 
            if len(price_yes) > 0 :
                price_c.append(price_yes)
        for i in price_neg : 
            price_neg_yes = [s for s in words if i in s] 
            if len(price_neg_yes) > 0 :
                price_neg_c.append(price_neg_yes)
        for i in gapoom_neg :
            gapoom_neg_yes = [s for s in words if i in s]
            if len(gapoom_neg_yes) > 0:
                gapoom_neg_c.append(gapoom_neg_yes)
        for i in light : 
            light_yes = [s for s in words if i in s] 
            if len(light_yes) > 0 :
                light_c.append(light_yes)
        for i in season : 
            season_yes = [s for s in words if i in s] 
            if len(season_yes) > 0 :
                season_c.append(season_yes)
        for i in hard_neg : 
            hard_neg_yes = [s for s in words if i in s] 
            if len(hard_neg_yes) > 0 :
                hard_neg_c.append(hard_neg_yes)
        for i in daily :
            daily_c_yes = [s for s in words if i in s]
            if len(daily_c_yes) > 0:
                daily_c.append(daily_c_yes)
        for i in design :
            design_c_yes = [s for s in words if i in s]
            if len(design_c_yes) > 0:
                design_c.append(design_c_yes)
        for i in color : 
            color_yes = [s for s in words if i in s] 
            if len(color_yes) > 0 :
                color_c.append(color_yes)
        for i in present :
            present_cyes = [s for s in words if i in s]
            if len(present_cyes) > 0:
                present_c.append(present_cyes)
        for i in mode : 
            mode_yes = [s for s in words if i in s] 
            if len(mode_yes) > 0 :
                mode_c.append(mode_yes)
        for i in feel : 
            feel_yes = [s for s in words if i in s] 
            if len(feel_yes) > 0 :
                feel_c.append(feel_yes)
        for i in feel_neg : 
            feel_neg_yes = [s for s in words if i in s] 
            if len(feel_neg_yes) > 0 :
                feel_neg_c.append(feel_neg_yes)
        for i in couple :
            couple_c_yes = [s for s in words if i in s]
            if len(couple_c_yes) > 0:
                couple_c .append(couple_c_yes)
        for i in quality_neg :
            quality_negc_yes = [s for s in words if i in s]
            if len(quality_negc_yes) > 0:
                quality_neg_c .append(quality_negc_yes)

    except Exception as e:
        print("에러문장")
        print(sentence)

df_positive = pd.DafaFrame(data= {'size_c' : len(size_c), \
'price_c' : len(price_c), \
'light_c' : len(light_c), \
'season_c' : len(season_c),\
'daily_c'  : len(daily_c),\
'design_c'  : len(design_c),\
'color_c'  : len(color_c),\
'present_c' : len(present_c),\
'mode_c' : len(mode_c),\
'feel_c' : len(feel_c),\
'couple_c' : len(couple_c)})

print(df_positive)

df_negative = pd.DafaFrame(data ={'quality_neg_c': len(quality_neg_c),\
'hard_neg_c' : len(hard_neg_c),\
'feel_neg_c': len(feel_neg_c),\
'price_neg_c'  : len(price_neg_c),\
'gapoom_neg_c' :  len(gapoom_neg_c)})

print(df_negative)




