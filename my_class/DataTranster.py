import pandas as pd

class DataTransfer:
    def __init__(self, root, file_name):
        self.root = root
        self.file_name = file_name
        
    def import_excel(self):
        load_data = pd.read_excel(self.root + self.file_name + '.xlsx')
        return load_data
    
    def export_excel(self, data):
        data.to_excel(self.root + self.file_name + '_result.xlsx')
        print('저장완료')
        
    def import_txt(self):
        f = open(self.root + self.file_name + '.txt', 'r', encoding='UTF8')
        text = f.read()
        return text 

data = DataTransfer('C:/Users/leevi/Desktop/데상트_3월/_무신사/', '무신사_크롤링_백팩')
data_result = data.import_excel()
#print(data_result)

#data02 = DataTransfer('C:/Users/leevi/Desktop/데상트_3월/_무신사/', 'data_result')
#data02.export_excel(data_result)

#data03 = DataTransfer('C:/Users/leevi/Desktop/데상트_3월/_무신사/', '무신사_리뷰_18')
#text01 = data03.import_txt()
#text01
