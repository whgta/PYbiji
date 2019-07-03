# Xpath
- 在xml文件中查找新的一套规则/语言，根据XML的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp

# Xpath 开发工具
- 开源的Xpath表达编辑工具：XMLQuire
- chorme插件：XPath Helper
- Firefox插件：XPath checker

# 选取节点
- nodename：选取此节点所有子节点
- /：从根节点开始选取
- //：选取节点，不考虑位置
- .：选取当前接待你
- ..：选取当前节点的父亲节点
- @：选取属性
- xpath中查找一般按照路径方法查

        School/Teacher：返回Teacher节点
        //Student：选取所有学生节点，不考虑位置
        School//age：选取school所有age节点
        //@OTher：选取Other属性
        //Age[@detail]:选取带有属性detail的age元素
        
# 谓语-Predicates
- /School/Student[1]:选取School下面第一个Student节点
- /School/Student[last()]:选取School下面最后一个Student节点
- /School/Student[last()-1]:选取School下面倒数第二Student节点
- //Student[@score]:选取带有属性score的Student节点
- //Student[@score="99"]:选取带有属性score并且值为99的Student节点
- //Student[@score]/age:选取带有属性score的Student节点的子节点age

# xpath的一些操作
- |：或者

    //Student[@score]|//Teacher:选取带有属性score的Student节点或者Teacher节点
