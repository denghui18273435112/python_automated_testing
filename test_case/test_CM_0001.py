from test_method.SongQin_API import  SongQin_API
import unittest
import HTMLTestRunner
sc = SongQin_API()

class test_CM_0001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         print("""\n\n*** steptest_CM_0001-00 ***\n""")

    @classmethod
    def tearDownClass(cls):
         print("""\n\n*** steptest_CM_0001-999 ***\n""")

    def setUp(self):
        print("""\n\n*** step0 ***\n""")

    def tearDown(self):
        """删除班级"""
        sc.delete_school_calss(self.ret1_id)
        print("""\n\n*** step4 *** 删除班级后再列出所有班，看看没有删除成功\n""")
        self.ret3 = sc.list_school_class()

    def tests_0001(self):
        """添加班级"""
        print("""\n\n*** step1 *** 添加7年级二班\n""")
        self.grade__name = "七年级"
        self.studentlimit = 60
        self.name = "2班"
        self.ret1 = sc.add_school_class(sc.grade_values_converted_nubers(self.grade__name),self.name,self.studentlimit )
        sc.new_assert(self.ret1["retcode"],0,"添加班级信息")

        print("""\n\n*** step2 ***取出班级添加成功后所返回的id invitecode值，便于对比\n""")
        self.ret1_id =self.ret1["id"]
        self.ret1_invitecode =self.ret1["invitecode"]

        print("""\n\n*** step3 *** 列出当前所有班级进行对比\n""")
        self.ret2 = sc.list_school_class()


class test_CM_0002(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         print("""\n\n*** steptest_CM_0002-00 ***\n""")

    @classmethod
    def tearDownClass(cls):
         print("""\n\n*** stepsteptest_CM_0002-999 ***\n""")


    def setUp(self):
        print("""\n\n*** step0 ***\n""")

    def tearDown(self):
        """删除班级"""
        sc.delete_school_calss(self.ret1_id)
        print("""\n\n*** step4 *** 删除班级后再列出所有班，看看没有删除成功\n""")
        self.ret3 = sc.list_school_class()

    def tests_0001(self):
        """添加班级"""
        print("""\n\n*** step1 *** 添加7年级二班\n""")
        self.grade__name = "七年级"
        self.studentlimit = 60
        self.name = "2班"
        self.ret1 = sc.add_school_class(sc.grade_values_converted_nubers(self.grade__name),self.name,self.studentlimit )
        sc.new_assert(self.ret1["retcode"],0,"添加班级信息")

        print("""\n\n*** step2 ***取出班级添加成功后所返回的id invitecode值，便于对比\n""")
        self.ret1_id =self.ret1["id"]
        self.ret1_invitecode =self.ret1["invitecode"]

        print("""\n\n*** step3 *** 列出当前所有班级进行对比\n""")
        self.ret2 = sc.list_school_class()




