from test_method.SongQin_API import  SongQin_API
import unittest
import HTMLTestRunner
sc = SongQin_API()

class test_setUpClass_tearDownClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         print("""\n\n*** step00 ***\n""")

    @classmethod
    def tearDownClass(cls):
         print("""\n\n*** step999 ***\n""")