import unittest
from calculate import add, sub
from clstest import Dog

class demo(unittest.TestCase):

    def test_add(self):
        self.assertEqual(10,add(3,7),msg="加法出错")

    def test_sub(self):
        self.assertEqual(3,sub(5,2),msg="减法出错")

    def test_catch(self):
        redDog = Dog('red',5)
        self.assertEqual("狗不能抓老鼠！", redDog.catch(), msg="catch方法出错")

    def test_woa(self):
        blueDog = Dog('blue',3)
        self.assertEqual('blue汪！我3岁了', blueDog.woa(), msg="woa出错")

if __name__=='__main__':
    unittest.main()
