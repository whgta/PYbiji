# 结构化文件存储
- xml，json
- 为了解决不同设备之间信息交换
- xml，人好读
- json
# XML文件
- 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
    
- XML()可扩展标记语言
    - 标记语言：语言中使用尖括号括起来的文字字符串标记
    - 可扩展：用户可以自己定义需要的标记
    - 例如：
    
            <Teather>
                自定义标记Teather
                在两个标记之间任何内容都应该跟Teather相关
            </Teather>
    - 是w3c组织制定的一个标准
    - XML描述的是数据本身，即数据的结构和语义
    - HTML侧重于如何显示web页面的数据
 
- XML文档的结构
    - 案例exam.xml
    - 处理指令（可以认为一个文件内只有一个处理指令）
        - 最多只有一行
        - 且只能在第一行
        - 内容是与xml本身处理起相关的一些声明或者指令
        - 以xml关键字开头
        - 一般用于声明XML的版本和采用的编码
            - version属性是必须的 
            - encoding属性用来指出xml解释器使用的编码
    - 根元素（一个文件内只有一个根元素）
        - 在整个xml文件中，可以把它看成树结构
        - 根元素有且只能有一个
    - 子元素
    - 属性
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 起说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头而不能公用在结尾
                    
                    <name> <!-- wanghao --> </name> #可以
                    <name <!-- wanghao -->> </name> #不可以，注释在标签内
                    
                    <!--my-name-by-wang--> #可以，注释内容可以有一个短横线
                    <!--my--name--by--wang--> #不可以，双横线只能出现在开头或者结尾
                    
                    <!---my-name--> #可以 三短横线只能出现在开头
                    <!---my-name---> #不可以 三短横线只能出现在开头
                    
- 保留字符的处理
    - XML中使用的符号可能跟实际符号相冲突，带女性的就是左右尖括号
    - 使用实体引用 （entity Reference）来表示保留字符
    
            <score> math>80 </score> # 有错误，xml中不能出现>
            <score> math&gt;80 </score># 使用实体引用
    - 把含有保留字符的部分放在CDATA块内部，CDATA块巴内部信息视为不需要转义
    
    - 常用的需要转义的保留字符和对应实体引用
            
            - &：&amp；
            - <:&lt;
            - >:&gt;
            - ':&apos;
            - ":&quot;
            - 一共五个，每个尸体引用都已&开头并且以分号结尾
            
- XML标签的命名规则
    - Pascal命名法
    - 用单词表示，第一个字母大写
    - 大小写严格区分
    - 配对的标签必须一致 
    
- 命名空间
    - 为了防止命名冲突
    - 平行的两个头标签中都有一个name的标签
    - 现在合并这两个头标签，为了避免，需要给可能冲突的元素添加命名空间
    - xmlns： xml name space 的缩写
    
            <schooler xmlns:student="http://my_student" xmlns:room="http://my_toom">
                # 原来的样子<name>wh</name>,仙子啊改成下面的：
                <student:name>wh</student:name>
                <room:name>151</room:name>
                
# XML访问

## 读取
- XML读取分两个主要技术，SAX，DOM
- SAX（simple API for XML）：
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器中时间处理两部分 
    -  特点：
        - 快
        - 流式读取             

- DOM
    - 是w3c规定的XML编程接口
    - 一个XML文件在缓存中以树形结构保存，读取
    - 用途
        - 定位浏览XML任何一个节点信息
        - 添加删除相关内容
    - minidom
        ....
        - 案例01，没写
    - etree  
        - 以树形结构来表示xml
        - root.getiterator:得到相应的可迭代的node集合
        - root.iter:
        - find(onde_name):查找指定node_name的节点，返回一个node
        - root.findall(node_name):返回多个node_name的节点
        - node.tag:node对应的tagename
        - node.text:node的文本值
        - node.attrib: 是node的属性的字典类型的内容
        - 案例02 
        
- xml文件写入
    - 更改
        - ele.set:修改属性 
        - ele.append:添加子元素
        - ele.remove:删除元素   
        - 案例03
    - 生成创建 
        - SubElement，案例04 
        - minidom写入
        - etree创建，案例06