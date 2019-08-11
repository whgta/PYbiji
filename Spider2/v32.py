from lxml import etree

# 只能读取xml格式内容，html报错
html = etree.parse("./v30.html")
print(html)

rst = html.xpath('//book')
print(type(rst))
print(rst)

# xpath的意思是，查找带有category属性值为cooking的book元素
rst = html.xpath('//book[@category="cooking"]')
print(type(rst))
print(rst)


rst = html.xpath('//book[@category="cooking"]/year')
rst = rst[0]
print(type(rst))
print(rst)
print(rst.tag)
print(rst.text)