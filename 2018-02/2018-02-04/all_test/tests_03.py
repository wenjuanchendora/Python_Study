import unittest

class MyTest3(unittest.TestCase):

    def test_up3(self):
        self.assertEqual("foo".upper(),'FOO')

    def test_isUp3(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("foo".isupper())

    def test_split3(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)
def main():      # verbosity 日志级别
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
