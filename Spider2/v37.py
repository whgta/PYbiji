'''
通过webdriver操作进行查找

这里要下载浏览器phantomjs
但我没下载  所以不能运行

'''

from selenium import webdriver
import time

# 通过keys模拟键盘
from selenium.webdriver.common.keys import Keys


# 操作哪个浏览器就对哪个浏览器建一个实例
# 自动按照环境变量查找相应的浏览器
driver = webdriver.PhantomJS()

# 如果浏览器没有相应环境变量中，需要指定浏览器位置

driver.get("http://www.baidu.com")

# 通过函数查找title标签
print("Title:{0}".format(driver.title))


