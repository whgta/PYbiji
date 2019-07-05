# 需要导入相应包，主要时ftplib
import ftplib
import os
import socket

# 三部分精确表示ftp服务器上的文件
# 好多公开的ftp服务器访问会出错或者没反应
HOST = "ftp.acc.umu.se"
DIR = "Public/EFLIB/"
FILE = "README"

# 1.客户端来连接远程主机上的服务器
try:
    f = ftplib.FTP()
    #通过设置调试级别可以方便调试
    f.set_debuglevel(2)
    #连接主机地址
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***connected to HOST {0}***".format(HOST))



#2.客户端输入用户名密码
try:
    # 登陆如果没有输入用户名信息，默认匿名 登陆
    f.login()
except Exception as e:
    print(e)
    exit()
print("***logging in as ***")

# 3.客户端服务端进行各种文件传输和信息查询操作
try:
    # 更改当前目录到指定目录
    f.cwd(DIR)
except Exception  as e:
    print(e)
    exit()
print("***changed dir to {0}".format(DIR))

try:
    # 从服务器上下载文件
    # 第一个参数时ftp命令
    # 第二个参数时回调函数
    # 此函数的意思时，执行RETR命令，下载文件到本地后，运行回调函数
    f.retrbinary("RETR {0}".format(FILE),open(FILE,'wb').write)
except Exception as e
    print(e)
    exit()

# 4.客户端从远程服务器推出结束传输
f.quit()