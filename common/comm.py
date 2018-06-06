from xlrd import open_workbook
from config import globalpara as gl


#读取excel数据，将每行数据存入列表
def get_xls(xls_name):
    #excel路径
    xls = gl.test_data + xls_name
    #打开excel
    file = open_workbook(xls)
    #第一个sheet页
    sheet = file.sheet_by_index(0)
    #获取总行数
    nrows = sheet.nrows
    cls = []
    for i in range(1,nrows):
        #插入每行数据
        cls.append(sheet.row_values(i))
    return cls

#print(get_xls('xiaowen_api.xlsx'))
