import json
from urllib.request import urlopen
import pandas as pd

def get_data(premium_url):
    try :
        data = urlopen(premium_url)
        mydatas = json.loads(data.read())
        #print(resp)

    except Exception as e:
        print("Error for URL")

    mycolumns = ['sort', 'content', 'user', 'star', 'date']
    df = pd.DataFrame(columns=mycolumns)
    for comment in mydatas['result']['ds_evalPremium']:
            p_list_comment = []
            p_list_comment.append('프리미엄댓글')
            p_list_comment.append(comment['contents'])
            p_list_comment.append(comment['nickname'])
            p_list_comment.append(comment['gradeRate'])
            p_list_comment.append(comment['insertDate'])
            new_df = pd.DataFrame([p_list_comment], columns=mycolumns)
            df = pd.concat([df, new_df])
    
    #print(df)
    return df 

def main():
    mycolumns = ['sort', 'content', 'user', 'star', 'date']
    data_result = pd.DataFrame(columns=mycolumns)
    premium_url1 = 'http://base.cjmall.com/api/item/52244933/premium-list.json?page='
    premium_url2 = '&option1Cd=&option2Cd=&sortGbn=&imgYn=&rowsPerPage=5'
    for i in range(1,800):
        page = str(i)
        premium_url = premium_url1 + page + premium_url2
        df = get_data(premium_url)
        data_result = pd.concat([data_result, df], axis=0)
    data_result.to_csv('C:/Users/leevi/Downloads/data_CJmall.csv', mode='w', encoding='utf-8', index=False)
    print('저장완료')


if __name__ == "__main__":
    main()
