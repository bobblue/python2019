#댓글에 특수문자 지우고 크롤링

import json
import requests
import pandas as pd
import re
from itertools import count

# 입력받은 URL을 바탕으로 jason 형식의 데이터를 요청한다
def get_request_url(url_all):
    try:
        response = requests.get(url_all)
        if int(response.status_code) == 200:
            p = re.compile('premium.json')
            if bool(p.search(url_all)) == True:
                print("PremiumComment Url Request Success")
                return response.text
            else:
                print("GeneralComment Url Request Success")
                return response.text
    except Exception as e:
        print(e)
        print("Error for URL")
        return None

# 일반상품평과 프리미엄 상품평으로 나누어서 데이터를 받아온다
def getComment(s_name, p_number):
    url01 = 'http://smartstore.naver.com/'
    url03 = '/products/'
    url05 = '/purchasereviews/premium.json?sortType=PURCHASE_REVIEW_CREATED&evaluationGrade=&page.page=1&page.size=999'
    url_all1 = url01 + s_name + url03 + p_number + url05

    url01 = 'http://smartstore.naver.com/'
    url03 = '/products/'
    url05 = '/purchasereviews/general.json?satisfactionGrade=&page.page=1&page.size=999'
    url_all2 = url01 + s_name + url03 + p_number + url05

    plain_text1 = get_request_url(url_all1)
    plain_text2 = get_request_url(url_all2)

    mydatas = []
    for i in [plain_text1, plain_text2]:
        if (i == None):
            return None
        else:
            mydatas.append(json.loads(i))

    return mydatas

# jason에서 만족도, 댓글 내용, 댓글 작성 날짜를 불러온다
def dataHandling(mydatas):
    p_list_comment = []

    for comment in mydatas[0]['htReturnValue']['pagedResult']['content']:
        p_list_comment.append('프리미엄댓글')
        p_list_comment.append(comment['gradeText'])
        p_list_comment.append(comment['contentsSummary'])
        p_list_comment.append(comment['createdDate'])

    g_list_comment = []

    for comment in mydatas[1]['htReturnValue']['pagedResult']['content']:
        g_list_comment.append('일반댓글')
        g_list_comment.append(comment['gradeText'])
        g_list_comment.append(comment['title'])
        g_list_comment.append(comment['createdDate'])

    result = []
    _result = []

    for i in [p_list_comment, g_list_comment]:
        for item in i:
            _result.append(item)
            if len(_result) == 4:
                result.append(_result)
                _result = []

    data = pd.DataFrame(result, columns=('type', 'prefer', 'content', 'date'))

    j = 0
    p = re.compile('\w+')
    for item in data['content']:
        b = item.replace('\n', '')
        c = p.findall(b)
        k = ''
        for i in c:
            k += ' ' + str(i)
        data['content'][j] = k
        j += 1

# 프리미엄 댓글과 일반 댓글의 형식을 맞추기 위해서 프리미엄의'적극추천','추천','추천안함'을 리코딩 한다
    j = 0
    for i in data['prefer']:
        if str(i) == '적극추천' or str(i) == '추천':
            data['prefer'][j] = '만족'
            j += 1
        elif str(i) == '추천안함':
            data['prefer'][j] = '불만'
            j += 1

    return data

# 입력받은 URL 에서 스토어명과 상품번호를 정규표현식을 통해 추출한다
def main():
    url = []
    p = re.compile('http://')
    for i in count():
        url.append(str(input('{0}번째 url을 입력하세요 : '.format(i+1))))
        # print(bool(p.search(url[i]).group()))
        #if p.search(url[i]) == None:
        #    url.remove(url[i])
        #    break

        _s_name = re.compile('\w+/products/')
        _p_number = re.compile('/products/\d+')

        s_name = str(_s_name.search(url[i]).group()).replace('/products/','')
        p_number = str(_p_number.search(url[i]).group()).replace('/products/','')
        print('스토어팜 이름: ' + s_name + '    /   상품 번호: ' + p_number)

        mydatas = getComment(s_name, p_number)

        data = dataHandling(mydatas)

        data.to_csv('data_%s_%s.csv'%(s_name,p_number), mode = 'w', encoding='utf-8', index= False)
        print('저장 완료')

if __name__ == "__main__":
    main()

