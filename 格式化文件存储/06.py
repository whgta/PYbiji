import xml.etree.ElementTree as et

# 在内存中创建一个空的文档

etree = et.ElementTree()
e = et.Element('Student')

etree._setroot(e)# 把这个e设成为根

e_name = et.SubElement(e,'Name')
e_name.text = 'hahah'

etree.write('v06.xml')