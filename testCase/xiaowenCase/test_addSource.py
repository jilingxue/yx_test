import requests
import unittest
from common.Log import Log
import random
from config import globalpara as gl

#config url
url = gl.xiaowen+'/v3/addSource'
#config data
def data(subject_id, type,sub_type):
    return {"subject_id": subject_id, "type": type, "source":'source %d'%random.randint(0000,9999),
            "create_user": "1", "grade": "", "sub_type": sub_type, "remake": "", "name": ""}


class TestAddSource(unittest.TestCase):

    def test_addSource_01(self):
        case_name = '测试添加英语资源，视频类型，知识点视频'
        json = requests.post(url=url,data=data(subject_id=1,type=100,sub_type=101)).json()
        self.assertEqual(json['code'],200)
        self.assertEqual(json['message'],'成功')
        self.mylog.info(case_name)


    def test_addSource_02(self):
        case_name = '测试添加数学资源，音频类型，试题听力音频'
        json = requests.post(url,data(2,200,201)).json()
        self.assertEqual(json['code'],200)
        self.assertEqual(json['message'],'成功')
        self.mylog.info(case_name)

    def test_addSource_03(self):
        case_name = '测试添加语文资源，图片类型，知识点讲义'
        json = requests.post(url,data(3,300,301)).json()
        self.assertEqual(json['code'],200)
        self.assertEqual(json['message'],'成功')
        self.mylog.info(case_name)

    def test_addSource_04(self):
        case_name = '测试添加物理资源，富文本类型，知识点讲义'
        json = requests.post(url,data(4,400,401)).json()
        self.assertEqual(json['code'],200)
        self.assertEqual(json['message'],'成功')
        self.mylog.info(case_name)




    def setUp(self):
        self.mylog = Log()
    def tearDown(self):
        print('--------------end--------------')
if __name__ == '__main__':
    unittest.main()



