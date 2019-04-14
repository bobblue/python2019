import json
from urllib.request import urlopen
import pandas as pd

# 일반 구매평
def get_data(normal_url):
    try:
        data = urlopen(normal_url)
        mydatas_ = json.loads(data.read())
        print('성공')
        print(mydatas_)
        mycolumns = ['sort', 'content', 'user', 'star', 'date']
        df = pd.DataFrame(columns=mycolumns)
        for comment in mydatas_['result']['ds_eval']:
            n_list_comment = []
            n_list_comment.append('일반댓글')
            n_list_comment.append(comment['mention'])
            n_list_comment.append(comment['nickname'])
            n_list_comment.append(comment['option2Nm'])
            n_list_comment.append(comment['insertDate'])
            print(n_list_comment)
            new_df = pd.DataFrame([n_list_comment], columns=mycolumns)
            df = pd.concat([df, new_df])
        return df

    except Exception as e:
        print("Error for URL")


# return df

def main():
    mycolumns = ['sort', 'content', 'user', 'star', 'date']
    data_result = pd.DataFrame(columns=mycolumns)
    normal_url1 = 'http://display.cjmall.com/api/item/52244933/inline-list.json?page='
    normal_url2 = '&option1Cd=&option2Cd=&sortGbn=&rowsPerPage=5'

    normal_url ='http://display.cjmall.com/api/item/52244933/inline-list.json?page=1&rowsPerPage=900'

    df = get_data(normal_url)
    data_result = pd.concat([data_result, df], axis=0)
    data_result.to_csv('C:/Users/leevi/Downloads/data_CJmall_normal.csv', mode='w', encoding='utf-8', index=False)
    print('저장완료')



if __name__ == "__main__":
    main()

