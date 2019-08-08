'''
爬取豆瓣电影数据
了解ajax基本爬法
'''

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
from urllib import request
import json

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)
print(data)