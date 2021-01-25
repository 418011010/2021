# -*- coding: utf-8 -*-
'''
    clstest.py
    类的使用
'''

mouseNum = 0
#创建类
class Dog():

    #初始化方法
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #定义叫方法
    def woa(self):
        #print("{}汪！我{}岁了".format(self.name,self.age))
        return "{}汪！我{}岁了".format(self.name,self.age)
    
    #定义吃方法
    def eat(self):
        global mouseNum
        if mouseNum >= 1:
            mouseNum -= 1
            print("{}吃了{}只老鼠，还剩{}只老鼠".format(self.name,1,mouseNum))
        else:
            print("老鼠数量不足")
    
    #定义抓方法
    def catch(self):
        #print("狗不能抓老鼠！")
        return "狗不能抓老鼠！"


#创建猫类
class Cat():
    #初始化方法
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #定义叫方法
    def miao(self):
        print("{}喵！我{}岁了".format(self.name,self.age))

    #定义抓方法
    def catch(self):
        global mouseNum
        mouseNum += 1
        print("抓到1只老鼠，现在有{}只老鼠".format(mouseNum))

if __name__ == '__main__':
    erha = Dog("二哈",3)
    kitty = Cat("凯蒂",4)
    print(erha.catch())
    erha.eat()
    erha.woa()
    kitty.miao()
    kitty.catch()
    erha.eat()

