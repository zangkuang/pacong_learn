# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/24  19:45 
# tool：PyCharm

import requests
import re

'''
信息标记的三种形式：xml，json，yaml
信息提取方法：
    完整解析信息的标记形式再提取关键信息
    无视标记形式，直接搜索关键信息
    融合：结合形式解析和搜索方法，提取关键信息
'''

from bs4 import BeautifulSoup
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
"""print(soup.find_all('a'))       #返回一个列表类型，存储查找的结果
for link in soup.find_all('a'):
    print(link.get('href'))
for link1 in soup.find_all(['a','b']):
    print(link1)"""

#对标签名称的检索字符
"""for item in soup.find_all(True):
    print(item.name)

import re
for item1 in soup.find_all(re.compile('b')):
    print(item1.name)"""

#对标签属性值的检索字符串，可标注属性检索
"""attr = soup.find_all('p','course')      #在标签内部去检索course字符
print(attr)
print(soup.find_all('link'))
print(soup.find_all(id = re.compile('link')))"""

#recursive是否对子孙全部检索，默认True
"""print(soup.find_all('a'))
print(soup.find_all('a',recursive=False))"""

#对内容进行检索
print(soup.find_all(string='Basic Python'))
print(soup.find_all(string=re.compile('python')))       #compile不区分大小写
print(soup(string=re.compile('python')))       #soup(..)等价于soup.find_all(..)
a = soup.find('a')
print(a(string=re.compile('python')))       #<tag>(..)等价于<tag>.find_all(..)






