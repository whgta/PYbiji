# 数据和 p01 一样 但是是和02 文件 说明别的例子
class Student():
    def __init__(self, name="NoName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi 欢迎来到图灵学院")

print("我是模块p01")