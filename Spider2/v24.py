'''
正则结果Match的使用案例
'''

import re

# 一下正则分成了两个组，以笑哭哦好为单位
s = r'([a-z]+) ([a-z]+)'
pattern =re.compile(s,re.I)# s.I表示忽略大小写

m = pattern.match("Hello world wide wbe")
# group（0）表示返回匹配成功的整个子串
s = m.group(0)
print(s)

a = m.span(0)# 返回匹配成功的整个子串的跨度
print(a)

# group(1)表示返回的第一个分组匹配成功的子串
s = m.group(1)
print(s)

a = m.span(1)# 返回匹配成功的第一个子串的跨度
print(a)

s = m.groups()# 所有的分组
print(s)