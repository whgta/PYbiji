# scrapy-shell
- https://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- shell
- 启动
    - windows：scrapy shell "url:xxxx"
    - 启动后自动下载指定url网页
    - 下载完成后，url的内容保存在response的变量中，如果需要，我们需要调用response
- response
    - 爬取到的内容保存在response中
    - response.body是网页的代码
    - response.headers是返回的http的头信息
    - response.xpath()允许使用xpath语法选择内容
    - response.css()允许使用css语法选定内容
- selector
    - 选择器，允许用户使用选择器来选择自己想要的内容
    - response.selector.xpath:response.xpath是selector.xpath的快捷方式
    - response.selector.css:response.css是他的快捷方式
    - selector.extract:把节点内容unicode形式返回
    - selector.re：允许用户通过正则选区内容
    