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
        "emali":"17315110762",
        "password":"582452951"
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    req = request.Request(url,data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/971470567/newsfeed/photo"

    #如果已经执行了login函数，则opener自动已经半酣相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()