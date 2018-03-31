import unittest
from all_test.tests_01 import MyTest1

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')

    def test_01(self):
        self.assertEqual(1,1)
    def test_02(self):
        self.assertTrue(4)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_01'))
    suite.addTest(WidgetTestCase('test_02'))
    suite.addTest(MyTest1('test_up1'))
    suite.addTest(MyTest1('test_isUp1'))
    suite.addTest(MyTest1('test_split1'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())