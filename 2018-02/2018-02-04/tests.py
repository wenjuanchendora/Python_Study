import unittest

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("打开浏览器")

    def setUp(self):
        print("登录")
    
    def test_up(self):
        self.assertEqual("foo".upper(),'FOO')

    def test_isUp(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("foo".isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        print("screen shot")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")

    
def main():      # verbosity 日志级别
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()


''' 运行脚本的命令行, 此方法不需要定义 main 方法 
python -m unittest tests.py

python -m unittest -v tests.py

运行单个方法 
python -m unittest tests.MyTest.test_isUp
python -m unittest -v tests.MyTest.test_isUp
'''