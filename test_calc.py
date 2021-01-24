import unittest
from calculate import sub, add

class demotestcase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,add(1,2),msg='测试失败时打印的信息')

    #@unittest.skip
    #@unittest.expectedFailure #标记失败，若此单元通过则测试failed，结果失败才为正常.
    def test_sub(self):
        self.assertEqual(5,sub(9,4),msg="测试失败")


if __name__=="__main__":
    unittest.main()
