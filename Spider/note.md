# 0.爬虫准备工作
- 参考资料
    - python网络数据采集，图灵工业出版
    - 精通Python爬虫框架SCrapy，人民有点出本社
    - [python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    - [scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
- 前提知识
    - url
    - http协议
    - web前端，html，css，js
    - re,xpath
    - xml
    
# 1.爬虫简介
- 网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），
是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。
另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两部内容
    
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- Python网络包简介
    - python2.x：urllib,urllib2,urllib3,httplib,httplib2,requests
    - python3.x：urllib,urllib3,httplib2,requests
    - python2：urllib和urllib2配合使用，或者requests
    - python3：urllib和requests
    
# 2.urllib
- 包含模块
    - urllib.request:打开和读取url
    - urllib.error:包含urllib.request产生的常见的错误，使用try捕捉
    - urllib.parse:包含解析url的方法
    - urllib.robotparse：解析robots.txt文件
    - 案例v01
    
- 网页编码问题解决
    - chardet：可以自动检测页面文件的编码格式，但是可能有错
    - 需要安装 pip install chardet
    - 案例v02
- urlopen 的返回对象
    - 案例v03
    - geturl:返回请求对象的url
    - info：请求反馈对象的meta信息
    - getcode：返回的http code
- request.date 的使用
    - 访问网络的两种方式
        - get：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案例v04
        - post：
            - 一般想服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果使用post信息，需要用到data参数
            - 使用post·意味着Http的请求头可能需要更改
                - Content-Type：application/x-www.form-urlencode
                - Content-Length：数据长度
                - 简而言之·一旦更改请求方法·请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例v05
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了  
            - 需要利用request.Request类
            -案例v06
            
- urllib.error
    - URLError产生的原因
        - 没网
        - 服务器连接失败
        - 不知道指定服务器
        - 是OSError的子类
        - 案例v07
    - HTTPError,是URLError的一个子类
        - 案例v08
        
    - 两者区别：
        - HTTPError是对应HTTP请求的返回码错误，如果返回错误码是400以上的，则依法这个错误
        - URLError对应一般是网络出现错误，包括url问题
        - 关系区别：OSError-URLError-HttPError
- UserAgent
    - UserAgent:用户代理简称，UA，属于heads的一部分，服务器通过UA来判断访问这身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    - 设置UA可以通过两种方法：
        - heads
        - add_header
        - 案例v09
        
- ProxyHandler处理（代理服务器）
    - 使用代理IP·是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com   
    - 代理用来隐藏真实的访问中·代理 也不允许频繁访问某一个固定网站，所以代理一定要很多很多
    - 基本使用步骤：
        1.设置代理地址
        2.创建ProxyHandler
        3.创建Opener
        4.安装Openr
    - 案例v10  
    
- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发送给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
- cookie呵session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不会超过4K，很多浏览器限制一个站点最多保存20个
- session的存放位置
    - 存在服务器端
    - 一般情况·session是放在内存中或者数据库中
    - 没有cookie登陆 案例v11,可以看到，没使用cookie则返回网页为未登录状态
- 用cookie登陆
    - 直接把cookie赋值下俩，然后手动放入请求头
    - 案例v12
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，cookieJar实例回收cookie将消失
        - FileCookieJar（filename,delayload=None,policy=None）:
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar（filename,delayload=None,policy=None）:
            - 创建与mocilla浏览器cookie.txt倩蓉filecookieJar实例
        - LwpCookieJar（filename,delayload=None,policy=None）:
            - 创建与libwww-perl标准倩蓉的Set.cookie3格式的FilecookieJar实例
        - 他们的关系从上往下
    - 利用cookieJar访问人人，案例v13
        - 自动使用cookie登陆，大致流程是
        - 打开登陆页面后自动通过用户名密码登陆
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登陆隐私页面
    - handler是Handler的实例，常用参看案例代码
        - 用来处理复杂请求
                 
                    # 创建ciikiejar的实例
                    cookie = cookiejar.CookieJar()
                    # 生成cookie的管理器
                    cookie_handler = request.HTTPCookieProcessor(cookie)
                    # 创建一个http请求guanlq
                    http_handler = request.HTTPHandler()
                    
                    # 生成https管理器
                    https_handler = request.HTTPSHandler()
                  
    - 创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
    - cookie作为一个变量，打印出来 ，案例v14
        - cookie的属性
            - name： 名称
            - value：值
            - domain：可以访问此cookie的域名
            - path：可以访问此cookie的页面路劲
            - expires：过期时间
            - size： 大小
            - Http字段
    - cookie的保存-Filecookiejar，案例v15
    - cookie的读取·案例v16
    
- SSL
    - SSL证书就是值遵循SSL安全套阶层协议的服务器数字证书
    - 美国网景公司开发
    - CA 是数字证书认证中心·是发放·管理·废除数字整数的收信人的第三方机构
    - 遇到不信任的SSL证书·需要单独处理·案例v17
    
- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是去md5值）
    - 经过加密传输就是密文，但是
    - 加密函数或者过程一定实在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法·就可以模拟处加密过程从而达到破解
    - 过程参看案例v18，v19
    
- ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般使用json格式
    - 案例·爬取豆瓣电影，案例v20

# Requests-献给人类
- HTTP for Humans,更简洁更友好
- 继承了urllib的所有特性
- 底层使用的是urllib3
- 开源地址：https://github.com/requests/requests
- 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
- 安装：pip install request
- get 请求
    - requests.get()
    - requests.request("get",url)
    - 可以带有headers和parmas参数
    - 案例v21
- get返回内容
    - 案例v22
    
- post 
    - rsp = requests.post(url,data=data)
    - 参看案例v23
    - data,headers要求dict类型
- proxy
    -    
        proxies = {
        "http":"address of proxy",
        "https":"address of proxy"
        }
        
        rsp = requests.request("get","http:xxxxxx",proxies=proxies)
    - 代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭    

- 用户验证
    - 代理验证
    
            #可能需要使用HTTP basic Auth，可以这样
            # 格式为 用户名：密码@代理地址：端口地址
            proxy = {"http":"china:123456@192.168.1.123:4444"}
            rsp =  requests.get("http://baidu.com",proxies=proxy)
- web客户端验证
    - 如果遇到web客户端验证，需要添加auth = （用户名，密码）
    
        auth = ("test1","12346")#授权信息
        rsp = requests.get("http://www.baidu.com",auth=auth)
- cookie
    - requests可以自动处理cookie信息
    
    
                rsp =  requests.get("http://xxxxxx")
                # 如果对方服务器给传递过来cookie信息，则可以通过反馈的cookie属性得到
                # 返回一个cookiejar实例
                cookiejar = rsp.cookies
                
                # 可以将cookiejar转换成字典形式
                cookiedict = reques.utils.dict_from_cookiejar(cookiejar)
                
- session
    - 跟服务器session不是一个东东
    - 模拟一次会话，从客户端浏览器连接服务器开始，到客户端浏览器断开
    - 能让我们跨请求是保持某些参数，比如在同一个session案例发出的 所有请求之间保持cookie
    
                    
                    # 创建session对象，可以保持cookie值
                    ss = requests.session()
                    
                    headers = {"User-Agetn":"xxxxxxxxxxxx"}
                    data = {"name":"xxxxxxxx"}
                    
                    # 此时，由创建的session管理请求，负责发出请求
                    ss.post("http://www.baidu.com",data=data,headeers=headers)
                    
                    rsp = ss.get("xxxxxxxxxx")
                    
- https请求验证ssl证书
    - 参数verify负责表示是否需要验证ss证书，默认是True
    -如果不需要验证ssl证书，则设置成Flash表示关闭
    
                
                rsp =requests.get("http://www.baidu.com",verify=Flase)
                # 如果用verify=True访问12306，会报错，因为证书不正确
                