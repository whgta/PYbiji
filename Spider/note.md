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
    - urllib.parse:包含即url的方法
    - urllib.robotparse：解析robots.txt文件
    - 案例v01
    
- 网页编码问题解决
    - chardet：可以自动检测页面文件的编码格式，但是可能有错
    - 需要安装 pip install chardet
    - 案例v02
    