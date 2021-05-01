# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/24  15:10 
# tool：PyCharm

import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, 'html.parser')
#标签
"""print(soup.prettify())  #返回整个html文件
print(soup.title)       #返回标签即标签中间的内容
print(soup.a)           #当有多个标签使，返回第一个
获取标签名字，可通过.parent获取父亲标签名
print(soup.a.parent)
print(soup.a.parent.name)"""
#属性
"""tag = soup.a
print(tag.attrs)            #返回标签属性，及尖括号中非标签内容
#a标签及内容 <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
print(tag.attrs['class'])   #可通过列表形式访问
print(type(tag.attrs))      #dict
print(type(tag))            #bs4.element.Tag,一个<tag>可以有0或多个属性，字典类型"""
#标签内非属性字符串<tag>.string
"""str = soup.a.string
print(str)
str1 = soup.p.string
print(str1)
print(type(str1))           #<class 'bs4.element.NavigableString'>"""
#标签内字符串得注释部分
"""newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is a comment</p>",'html.parser')
zhushi = newsoup.b.string
print(zhushi)
print(type(zhushi))     #<class 'bs4.element.Comment'>  comment标签内得注释部分
print(newsoup.p.string)
print(type(newsoup.p.string))   #<class 'bs4.element.NavigableString'>"""

#下行遍历

#contents
"""
head = soup.head
print(head)
print(head.contents)
print(soup.body.contents)
print(len(soup.body.contents))#5 将tag所有儿子节点存入列表
print(soup.body.contents[1])        #该列表从1开始"""
#children
"""
for child in soup.body.children:     #遍历儿子节点
    print(child)
"""
#descendants
"""
for grandchildren in soup.body.descendants:     #遍历子孙节点，直到没有
    print(grandchildren)"""

#上行遍历
"""
# parent = soup.title.parent
# print(parent)
# print(soup.html.parent)     #html的父亲为整个文件
# print(soup.parent)
for parent in soup.a.parents:       #parents节点先辈标签的迭代类型,用于循环遍历先辈节点
    if parent is None:
        print(parent)
    else:
        print(parent.name)"""

#平行遍历_发生在同一个父节点下的各个节点
"""balace = soup.a.next_sibling
#实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白
# 因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
print(balace)     # and
print(balace.next_sibling)
print(soup.a.previous_sibling)  #实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白
print(soup.a.previous_sibling.previous_sibling) #None
print(soup.a.parent)

for sibling in soup.a.next_siblings:        #遍历后续节点
    print(sibling)

for sibling1 in soup.a.previous_siblings:   #遍历前序节点
    print(sibling1)"""

#HTML格式化输出
"""# print(soup)     #输出格式不好看
print(soup.prettify())      #.prettify()为HTML文本<>及其内容增加更加'\n'
# .prettify()可用于标签，方法：<tag>.prettify()
print(soup.a.prettify())
"""

#编码_bs4库将任何HTML输入都变成utf‐8编码Python3.x默认支持编码是utf‐8,解析无障碍
soup1 = BeautifulSoup('<p>中文</p>',"html.parser")
print(soup1.p.string)
print(soup1.p.prettify())



