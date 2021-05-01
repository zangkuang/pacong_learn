# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/24  10:40 
# tool：PyCharm

import requests
#通用代码框架
"""import requests
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url,headers = kv,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return '产生异常'
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))"""

#百度关键词搜索
"""def getHTMLText(url):
    try:
        head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        kv = {'wd':'Python'}
        response = requests.get(url,headers = head,params=kv,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        return len(response.text),response.status_code
    except:
        return '产生异常'
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))"""

#图片爬取和保存with open（‘path’，‘wb’） as f：f.write(content)
'''def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url,headers = kv,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        with open('picture','wb') as f:
            f.write(response.content)
        return response.status_code
    except:
        return '产生异常'
if __name__ == '__main__':
    url = 'https://bdyingxiaocms.cdn.bcebos.com/20210422/6081595222be8.jpg'
    print(getHTMLText(url))'''
#图片爬取2
"""r = requests.get('https://bdyingxiaocms.cdn.bcebos.com/20210422/6081595222be8.jpg')
print(r.status_code)
with open('picture','wb') as f:
    f.write(r.content)"""
#图片爬取3
'''import os
url = 'https://bdyingxiaocms.cdn.bcebos.com/20210422/6081595222be8.jpg'
root = 'E://github_project//pacong_learn//临时文件//'
path = root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        kv = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url,headers = kv,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        with open(path,'wb') as f:
            f.write(response.content)
            f.close()
            print('文件保存成功')
except:
    print('产生异常')'''

url = 'http://m.ip138.com/asp?ip='
kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
r = requests.get(url+'202.204.80.112',headers=kv)
r.encoding=r.apparent_encoding
# txt = r.text(encoding='utf-8')
print(r.text)