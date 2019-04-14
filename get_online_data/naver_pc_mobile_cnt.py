# 네이버 광고 사이트 '키워드' 검색량 분석

import pandas as pd


def read_json_list(root):

    # 파일로 넣을 때에는 주석과 같이 사용
    #data = pd.read_excel(root + 'naver_json_list.xlsx')
    #filenamelsit = list(data['filename'])
    #jsonlist = list(data['json'])

    filenamelist = ['노스페이스백팩', '데상트백팩', '휠라백팩'] 

    json1 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[9,9,160,170,130,220,70,200,120,200,230,160,30,70],"monthlyMobileQcCnt":[720,130,14500,4160,4200,2700,1190,1330,3560,1800,8040,1930,780,500],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"노스페이스백팩","monthlyProgressList":{"monthlyProgressPcQcCnt":[3960,2470,2130,2010,1890,2080,2430,2190,2350,2040,2090,3700,6810],"monthlyProgressMobileQcCnt":[21300,11100,8560,9550,9720,9810,12800,12600,11300,9530,11800,25300,53000],"monthlyLabel":["2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02"]}}]}
    json2 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[10,10,160,170,70,80,60,80,130,120,430,280,40,60],"monthlyMobileQcCnt":[1090,300,11100,3240,2060,910,960,510,3910,1030,10800,2400,790,430],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"데상트백팩","monthlyProgressList":{"monthlyProgressPcQcCnt":[19000,2770,1540,1220,1240,1320,1360,1220,1240,1340,1720,5280,8070],"monthlyProgressMobileQcCnt":[57500,14000,6900,5780,6040,6350,7430,7030,6310,6610,11100,29000,45900],"monthlyLabel":["2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02"]}}]}
    json3 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[30,6,440,220,250,220,140,100,130,100,340,140,50,50],"monthlyMobileQcCnt":[3880,280,22700,3320,4150,890,1230,360,3640,700,11100,2330,1010,600],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"휠라백팩","monthlyProgressList":{"monthlyProgressPcQcCnt":[11100,2980,1080,920,1140,1420,1580,1300,1030,1440,1600,5330,11300],"monthlyProgressMobileQcCnt":[98100,20000,7230,5930,8310,8830,11000,9980,7500,8360,13000,42800,70300],"monthlyLabel":["2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02"]}}]}
    jsonlist = [json1, json2, json3]

    return filenamelist, jsonlist

def data_to_df(json):
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

    f_json = {'10대' : {'f_pc' : sum(f.loc[0:3, :]['month_pc']), "f_mobile" : sum(f.loc[0:3, :]['month_mobile'])} }
    f_json.update({'20대' : {'f_pc' : sum(f.loc[4:7, :]['month_pc']), "f_mobile" : sum(f.loc[4:7, :]['month_mobile']) }})
    f_json.update({'30대' : {'f_pc' : sum(f.loc[8:9, :]['month_pc']), "f_mobile" : sum(f.loc[8:9, :]['month_mobile']) }})
    f_json.update({'40대이상' : {'f_pc' :sum(f.loc[10:, :]['month_pc']), "f_mobile" :sum(f.loc[10:, :]['month_mobile']) }})

    print('여성 검색량(최근 한 달)')
    print(pd.DataFrame(f_json))
    print('---------------'*3)
    print()

    m_json = {'10대' : {'m_pc' : sum(m.loc[0:3, :]['month_pc']), "m_mobile" : sum(m.loc[0:3, :]['month_mobile'])} }
    m_json.update({'20대' : {'m_pc' : sum(m.loc[4:7, :]['month_pc']), "m_mobile" : sum(m.loc[4:7, :]['month_mobile']) }})
    m_json.update({'30대' : {'m_pc' : sum(m.loc[8:9, :]['month_pc']), "m_mobile" : sum(m.loc[8:9, :]['month_mobile']) }})
    m_json.update({'40대이상' : {'m_pc' :sum(m.loc[10:, :]['month_pc']), "m_mobile" :sum(m.loc[10:, :]['month_mobile']) }})

    print('남성 검색량(최근 한 달)')
    print(pd.DataFrame(m_json))

    return year_df, f_json, m_json

def save_datafile(year_df, f_json, m_json, root, filename, writer):
    year_df.to_excel(writer, sheet_name=filename)  # Default position, cell A1.
    pd.DataFrame(f_json).to_excel(writer, sheet_name=filename, startcol=0, startrow = 16)
    pd.DataFrame(m_json).to_excel(writer, sheet_name=filename, startcol=0, startrow = 21)
    print('하하')
    return None

def main():
    filenamelist, jsonlist = read_json_list(root)
    
    with pd.ExcelWriter(root + 'naverkeyword_cnt.xlsx') as writer:
        for idx, json in enumerate(jsonlist) :
            filename = filenamelist[idx]
            year_df, f_json, m_json = data_to_df(json)
            save_datafile(year_df, f_json, m_json, root, filename, writer)

if __name__ == "__main__":
    root = 'C:/Users/leevi/Desktop/데상트_3월/'
    main()

