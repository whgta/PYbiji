
# 包含一个学生类，
# 一个打印语句
# 一个sayhello函数

class Student():
    def __init__(self, name="NoName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi 欢迎来到图灵学院")

# 此判断语句建议一致作为程序的入口
# 相当于第一句可执行的代码
# 不记得再看一遍视频 33课时62分钟位置
if __name__ == '__main__':
    print("我是模块p01")
