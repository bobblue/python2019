import pandas as pd

json = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[10,7,360,310,360,440,240,320,190,340,230,150,60,80],"monthlyMobileQcCnt":[430,230,14200,5590,7960,3830,2880,2200,4670,2840,6100,1750,1070,620],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"나이키백팩","monthlyProgressList":{"monthlyProgressPcQcCnt":[8840,5470,4640,3970,4060,4580,6680,6040,6850,5480,4010,8110,12200],"monthlyProgressMobileQcCnt":[54600,27400,19700,18300,19600,22400,31800,28900,28100,22600,25200,44100,62400],"monthlyLabel":["2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02"]}}]}

info = json['keywordList']

month_pc = info[0]['userStat']['monthlyPcQcCnt']
month_mobile = info[0]['userStat']['monthlyMobileQcCnt']
date = info[0]['userStat']['ageGroup']
gender = info[0]['userStat']['genderType']

oneyear_pc = info[0]['monthlyProgressList']['monthlyProgressPcQcCnt']
oneyear_mobile = info[0]['monthlyProgressList']['monthlyProgressMobileQcCnt']
oneyear_date = info[0]['monthlyProgressList']['monthlyLabel']

title = info[0]['relKeyword']

month_df = pd.DataFrame({'date':date, 'gender':gender, 'month_pc':month_pc, 'month_mobile':month_mobile})
print(month_df)

year_df = pd.DataFrame({'month':oneyear_date, 'pc':oneyear_pc, 'mobile':oneyear_mobile})
print(year_df)
