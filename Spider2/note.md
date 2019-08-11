# 页面姐西和数据提取
- 结构数据：先有结构，再谈数据
    - JSON文件
        - JSONPath
        - 转换成Python类型进行处理（json类）
    - XML文件
        - 转成成python类型（xmltodict）
        - XPath
        - CSS选择器
        - 正则
- 非结构化数据：先有数据，再谈结构
    - 文本
    - 电话号码
    - 邮箱地址
        - 通常处理此类数据，使用正则表达式
    -Html文件
        - 正则
        - XPath
        - CSS选择器
        
# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
- 案例v23，re的基本使用流程
- 案例v24，match的基本使用
- 正则常用方法：
    - match：从开始位置开始查找，一次匹配
    - search：从任何位置查找，一次匹配案例v25
    - findall：全部匹配，返回列表,案例v26
    - finditer：全部匹配，返回迭代器案例v26
    - split：分割字符串返回列表
    - sub：替换
- 匹配中文
    - 中文unicode范围主要在[u4e00-u9fa5]
    - 案例v27
    
- 贪婪与非贪婪模式
    - 贪婪模式：在整个表达式匹配成功后的前提下，尽可能多的匹配
    - 非贪婪模式：xxxxxxxxxxxxx，尽可能少的匹配
    - python里面数量词默认为贪婪模式
    - 例如：
        - 查找文本abbbbbbccc
        - re是ab*
        - 贪婪模式：结果是abbbbbb
        - 非贪婪：结果是a
        
# XML
- XML
- http://www.w3school.com.cn/xml/index.asp
- 案例v28.xml
- 概念：父节点·子节点·先辈节点·兄弟节点·后代节点

# XPath
- XPath，是一门在XML文档中查找信息的语言
- 官方文档：http://w3school.com.cn/xpath/index.asp
-  XPath开发工具
    - 开源的XPath表达式工具：XMLQuire
    - chorme插件：XPath Helper
    
- 常用路径表达式：
    - nodename：选取此节点所有子节点
    - /：从根节点开始选
    - //：选取元素·而不考虑元素的具体位置
    - .:当前节点
    - ..：父节点
    - @：选择属性
    - 案例：
        - bookstore：选取bookstore下的所有子节点
        - /bookstore：选取根元素
        - /bookstore/book：选取bookstore的所有book的子元素
        - //book：选取book子元素
        - //@lang：选取名称为lang的所有属性
- 谓语
    - 谓语用来查找某个特定的节点·被向前在方括号中
    - /bookstore/book[1]：选取第一个属于bookstore下叫book的元素
    - /bookstore/book[last()]：选取最后一个属于bookstore下叫book的元素
    - /bookstore/book[last()-1]：选取倒数第二个属于bookstore下叫book的元素
    - /bookstore/book[position()<3]：选取属于bookstore下叫book前两个的元素
    - /bookstore/book[@lang]：选取属于bookstore下叫book的，含有属性lang元素
    - /bookstore/book[@lang="cn"]：选取属于bookstore下叫book的，含有属性lang的值是cn的元素

- 通配符
    - '*'：任何元素节点
    - @*：匹配任何属性节点
    - node():匹配任何类型的节点
- 选取多个路径
    - //book/title  | //book/author：选取book元素中title和author元素
    
#lxml库
- python的HTML/XML的解析库
- 官方文档：http://lxml.de/index.html
- 案例v29
- 功能：
    - 解析HTML·案例v29
    - 文档读取·案例v30.html,v31.py
    - etree和XPath的配合使用，案例v32
    
    

        
    
    