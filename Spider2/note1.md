# 动态HTML

## 爬虫跟反爬虫

## 动态HTML介绍
- Javascript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从Javascript代码入手采集
    - python第三方库运行Javascript·直接采集你在浏览器看到的页面
    
## Selenium + PhantomJS
- Selenium：web自动化检测工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium==2.48.0
    - 官网：http://selenium-python.readthedocs.io/index.html
    
- PhantomJS（幽灵）
    - 基于Webkit的无界面的浏览器
    - 官网:http://phantomjs.org/download.html
- Selenuim 库有一个webDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以运行爬取
- 案例v37

- chrome + chromedriver
    - 下载安装chrome
    - 下载安装chromedriver：
- Selenium操作主要分两大类
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionChains类来做到
    - 案例v38
