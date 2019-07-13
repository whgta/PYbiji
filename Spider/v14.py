from urllib import request,parse
from http import cookiejar

# 创建ciikiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建一个http请求guanlq
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)


def login():
    '''
    负责初次登陆
    需要输入用户名密码，用来获取登陆cookie凭证
    :return:
    '''
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登陆form的两个对应unput中提取name属性
    data = {
        "emali":"13119144223",
        "password":"123456"
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    req = request.Request(url,data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    '''
    执行完login之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    login()
    print(cookie)
    for item in cookie:
        print(item)
        print(type(item))
        for i in dir(item):
            print(i)

