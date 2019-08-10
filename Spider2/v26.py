'''
findall
'''

import re



pattern = re.compile(r'\d+')# s.I表示忽略大小写

s = pattern.findall("i am 18 years old and 185 high")
print(s)

s = pattern.finditer("i am 18 years old and 185 high")
print(s)

for i in s:
    print(i.group())