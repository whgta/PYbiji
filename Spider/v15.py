from urllib import request,parse
from http import cookiejar

# 创建Filecookiejar的实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
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
    # 保存cookie文件
    # ignore_discard表示即使cookie将要被丢弃也要保存下来
    # ignore_expires表示如果该文件中cookie即使已经过期，保存
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()
