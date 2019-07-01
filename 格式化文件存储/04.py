import xml.etree.ElementTree as et

stu = et.Element("Student1")# 生成了一个元素Student1

name = et.SubElement(stu,'Name')# 又生成一个子元素，Sub是子的意思
name.attrib = {'lang':'en'}# Name子元素的属性
name.text = 'wh'

age = et.SubElement(stu,'Age')
age.text = '18'

et.dump(stu)