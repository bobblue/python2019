# 네이버 광고 사이트 '키워드' 검색량 분석

import pandas as pd


def read_json_list(root):

    # 파일로 넣을 때에는 주석과 같이 사용
    #data = pd.read_excel(root + 'naver_json_list.xlsx')
    #filenamelsit = list(data['filename'])
    #jsonlist = list(data['json'])

    filenamelist = ['한샘']
    json1 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[6,6,310,110,1360,890,3270,3470,5690,7340,2420,3850,780,1510],"monthlyMobileQcCnt":[140,50,7790,2610,7310,3190,14600,9440,44200,28800,20500,19200,9260,11100],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"한샘","monthlyProgressList":{"monthlyProgressPcQcCnt":[113800,97900,76900,81200,134500,74600,170200,105700,86800,92900,86800,89700,93100],"monthlyProgressMobileQcCnt":[225200,195800,151800,154200,225900,156800,325700,222400,214600,224700,232000,226100,215800],"monthlyLabel":["2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04"]}}]}
    #json2 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[4,2,150,40,510,270,1450,810,3990,2670,2030,1960,410,590],"monthlyMobileQcCnt":[170,50,1380,610,2480,800,7950,2330,52700,11300,27100,7320,3590,1460],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"일룸","monthlyProgressList":{"monthlyProgressPcQcCnt":[52400,51600,46400,48800,60400,52100,59800,51000,49000,62000,55900,55100,45400],"monthlyProgressMobileQcCnt":[131500,133800,120200,123400,175700,155500,159000,150300,178500,237100,235900,203600,131200],"monthlyLabel":["2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04"]}}]}
    #json3 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[2,1,50,10,270,90,1440,560,2690,2250,870,1050,240,320],"monthlyMobileQcCnt":[20,10,310,130,1650,390,9480,2100,30300,8540,10100,3440,2270,840],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"리바트","monthlyProgressList":{"monthlyProgressPcQcCnt":[44400,39100,31500,33500,37000,31700,39400,33000,29300,35100,29300,29200,28000],"monthlyProgressMobileQcCnt":[109800,97600,81200,77300,84500,82700,101700,93700,99600,116700,114300,105700,76600],"monthlyLabel":["2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04"]}}]}
    #json4 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[10,20,1070,490,4190,2930,9540,7490,16700,16700,6440,7240,1970,2670],"monthlyMobileQcCnt":[460,150,12300,4140,33400,11900,55900,23600,151500,50900,63800,21900,16400,7370],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"이케아","monthlyProgressList":{"monthlyProgressPcQcCnt":[258800,236400,224200,211800,229400,207400,259300,249200,229500,242500,218000,226000,201400],"monthlyProgressMobileQcCnt":[628200,561500,580400,526400,582100,572300,664400,633200,664700,678800,693300,653300,502300],"monthlyLabel":["2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04"]}}]}
    #json5 = {"keywordList":[{"userStat":{"monthlyPcQcCnt":[10,20,540,1070,1190,1160,1500,2490,1210,3040,1050,2070,370,760],"monthlyMobileQcCnt":[670,680,27700,27000,12800,9590,10300,10300,20700,20700,26000,18900,5800,5280],"genderType":["f","m","f","m","f","m","f","m","f","m","f","m","f","m"],"ageGroup":["0-12","0-12","13-19","13-19","20-24","20-24","25-29","25-29","30-39","30-39","40-49","40-49","50-","50-"]},"relKeyword":"데상트","monthlyProgressList":{"monthlyProgressPcQcCnt":[77300,74100,63300,67800,65100,82300,111200,111100,81300,66400,58900,64800,60600],"monthlyProgressMobileQcCnt":[228000,225700,209100,233200,243300,336500,444500,417000,351200,286300,314700,272900,236100],"monthlyLabel":["2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04"]}}]}

    jsonlist = [json1]

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
    print(f)
    print(m)
    print('---')

    f_json = {'10대' : {'f_pc' : sum(f.loc[0:3, :]['month_pc']), "f_mobile" : sum(f.loc[0:3, :]['month_mobile'])} }
    f_json.update({'20대' : {'f_pc' : sum(f.loc[4:7, :]['month_pc']), "f_mobile" : sum(f.loc[4:7, :]['month_mobile']) }})
    f_json.update({'30대' : {'f_pc' : sum(f.loc[8:9, :]['month_pc']), "f_mobile" : sum(f.loc[8:9, :]['month_mobile']) }})
    f_json.update({'40대' : {'f_pc' :sum(f.loc[10:11, :]['month_pc']), "f_mobile" :sum(f.loc[10:11, :]['month_mobile']) }})
    f_json.update({'50대' : {'f_pc' :sum(f.loc[12:13, :]['month_pc']), "f_mobile" :sum(f.loc[12:13, :]['month_mobile']) }})

    print('여성 검색량(최근 한 달)')
    print(pd.DataFrame(f_json))
    print('---------------'*3)
    print()

    m_json = {'10대' : {'m_pc' : sum(m.loc[0:3, :]['month_pc']), "m_mobile" : sum(m.loc[0:3, :]['month_mobile'])} }
    m_json.update({'20대' : {'m_pc' : sum(m.loc[4:7, :]['month_pc']), "m_mobile" : sum(m.loc[4:7, :]['month_mobile']) }})
    m_json.update({'30대' : {'m_pc' : sum(m.loc[8:9, :]['month_pc']), "m_mobile" : sum(m.loc[8:9, :]['month_mobile']) }})
    m_json.update({'40대' : {'m_pc' :sum(m.loc[10:11, :]['month_pc']), "m_mobile" :sum(m.loc[10:11, :]['month_mobile']) }})
    m_json.update({'50대' : {'m_pc' :sum(m.loc[12:13, :]['month_pc']), "m_mobile" :sum(m.loc[12:13, :]['month_mobile']) }})


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
    
    filename = '5월3일데이터'
    with pd.ExcelWriter(root + '{}_네이버광고_검색량.xlsx'.format(filename)) as writer:
        for idx, json in enumerate(jsonlist) :
            filename = filenamelist[idx]
            year_df, f_json, m_json = data_to_df(json)
            save_datafile(year_df, f_json, m_json, root, filename, writer)
    print('저장완료')

if __name__ == "__main__":
    root = 'C:/Users/leevi/Downloads/'
    main()
