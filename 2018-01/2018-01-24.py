"""
unittest

"""

import unittest

class CnodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("this is setUpClass...")

    def setUp(self):
        print("this is setup...")

    def test_01register(self):
        print("test_01register")
        # pass

    def test_02login(self):
        print("test_02login")
        # self.assertEqual(1,2)
        # pass

    def tearDown(self):
        print("this is teardown...")

    @classmethod
    def tearDownClass(self):
        print("this is tearDownClass...")




if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2)
