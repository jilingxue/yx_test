from config import configHttp
from common.comm import get_xls
from config import globalpara as gl
import unittest
from common.Log import Log
from ddt import ddt,data,unpack


request= configHttp.ConfigHttp()

@ddt
class TestApi(unittest.TestCase):

    @data(*get_xls('xiaowen.xlsx'))
    @unpack
    def test_search(self,url,data,msg,case_name):
        request.set_url(gl.xiaowen,url)      #config url
        request.set_data(data)               #config data
        self.case_name = case_name           #config casename
        self.response = request.post()       #get response
        #print(self.response)
        self.js = self.response.json()
        print('返回json：'+self.js)
        self.assertEqual(self.js['code'], 200)    # assert statues_code
        self.assertEqual(self.js['message'], msg)        #assert msg





    def setUp(self):
        self.mylog = Log()

        print('------------start api----------------')
    def tearDown(self):
        self.mylog.info('执行用例：{}'.format(self.case_name))
        print('-------------test end----------------')

if __name__ == '__main__':
    unittest.main()
