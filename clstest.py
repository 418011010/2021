# -*- coding: utf-8 -*-
'''
    clstest.py
    类的使用
'''

mouse_num = 0

#创建类
class Dog():

    #类的构造方法
    def __init__(self,name,age):
        #定义类的实例变量
        self.name = name
        self.age = age

    #定义叫方法
    def woa(self):
        #print("{}汪！我{}岁了".format(self.name,self.age))
        return "{}汪！我{}岁了".format(self.name,self.age)
    
    #定义吃方法
    def eat(self):
        global mouse_num
        if mouse_num >= 1:
            mouse_num -= 1
            print("{}吃了{}只老鼠，还剩{}只老鼠".format(self.name,1,mouse_num))
        else:
            print("老鼠数量不足")
    
    #定义抓方法
    def catch(self):
        #print("狗不能抓老鼠！")
        return "狗不能抓老鼠！"


#创建猫类
class Cat():

    #类的构造方法
    def __init__(self,name,age):
        #定义类的实例变量
        self.name = name
        self.age = age

    #定义叫方法
    def miao(self):
        print("{}喵！我{}岁了".format(self.name,self.age))

    #定义抓方法
    def catch(self):
        global mouse_num
        mouse_num += 1
        print("{}抓到1只老鼠，现在有{}只老鼠".format(self.name,mouse_num))

def main():
    erha = Dog("二哈",3)
    kitty = Cat("凯蒂",4)
    print(erha.catch())
    erha.eat()
    print(erha.woa())
    kitty.miao()
    kitty.catch()
    erha.eat()

if __name__ == '__main__':
    main()
    
