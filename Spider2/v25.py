'''
search
'''

import re


s = r'\d+'
pattern = re.compile(s)# s.I表示忽略大小写

m = pattern.search("one12two34three56")
print(m.group())


m = pattern.search("one12two34three56",10,40)
print(m.group())