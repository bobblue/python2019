import pandas as pd

json = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[20,30,750,1260,720,1260,940,1700,1080,2510,1150,1930,290,670],"monthlyMobileQcCnt":[2300,1580,45100,37700,16100,12500,11900,11300,26200,23100,35800,23100,6890,6320],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"데상트","monthlyProgressList":{"monthlyProgressPcQcCnt":[83600,83900,77300,74100,63300,67800,65100,82300,111200,111100,81300,66400,58900],"monthlyProgressMobileQcCnt":[310400,242200,228000,225700,209100,233200,243300,336500,444500,417000,351200,286300,314700],"monthlyLabel":["2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02"]}}]}
info = json['keywordList']

month_pc = info[0]['userStat']['monthlyPcQcCnt']
month_mobile = info[0]['userStat']['monthlyMobileQcCnt']
age = info[0]['userStat']['ageGroup']
gender = info[0]['userStat']['genderType']

oneyear_pc = info[0]['monthlyProgressList']['monthlyProgressPcQcCnt']
oneyear_mobile = info[0]['monthlyProgressList']['monthlyProgressMobileQcCnt']
oneyear_date = info[0]['monthlyProgressList']['monthlyLabel']

title = info[0]['relKeyword']

month_df = pd.DataFrame({'age':age, 'gender':gender, 'month_pc':month_pc, 'month_mobile':month_mobile})
#print(month_df)

year_df = pd.DataFrame({'month':oneyear_date, 'pc':oneyear_pc, 'mobile':oneyear_mobile})
print('월별 검색량 변화량')
print(year_df)
print('---------------'*3)
print()

f = month_df.loc[month_df ['gender'] == 'f', :]
m = month_df.loc[month_df ['gender'] == 'm', :]

f_json = {'10대' : {'pc' : sum(f.loc[0:2, :]['month_pc']), "mobile" : sum(f.loc[0:2, :]['month_mobile'])} }
f_json.update({'20대' : {'pc' : sum(f.loc[3:6, :]['month_pc']), "mobile" : sum(f.loc[3:6, :]['month_mobile']) }})
f_json.update({'30대' : {'pc' : sum(f.loc[7:9, :]['month_pc']), "mobile" : sum(f.loc[7:9, :]['month_mobile']) }})
f_json.update({'40대이상' : {'pc' :sum(f.loc[10:, :]['month_pc']), "mobile" :sum(f.loc[10:, :]['month_mobile']) }})

print('여성 검색량(최근 한 달)')
print(pd.DataFrame(f_json))
print('---------------'*3)
print()

m_json = {'10대' : {'pc' : sum(m.loc[0:2, :]['month_pc']), "mobile" : sum(m.loc[0:2, :]['month_mobile'])} }
m_json.update({'20대' : {'pc' : sum(m.loc[3:6, :]['month_pc']), "mobile" : sum(m.loc[3:6, :]['month_mobile']) }})
m_json.update({'30대' : {'pc' : sum(m.loc[7:9, :]['month_pc']), "mobile" : sum(m.loc[7:9, :]['month_mobile']) }})
m_json.update({'40대이상' : {'pc' :sum(m.loc[10:, :]['month_pc']), "mobile" :sum(m.loc[10:, :]['month_mobile']) }})

print('남성 검색량(최근 한 달)')
print(pd.DataFrame(m_json))
