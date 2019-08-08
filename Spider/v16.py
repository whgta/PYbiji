from urllib import request,parse
from http import cookiejar

# 创建Filecookiejar的实例

cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt",ignore_discard=True,ignore_expires=True)

# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建一个http请求guanlq
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def getHomePage():
    url = "http://www.renren.com/971470567/newsfeed/photo"

    #如果已经执行了login函数，则opener自动已经半酣相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)


if __name__ == '__main__':
    getHomePage()

