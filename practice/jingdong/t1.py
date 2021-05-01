# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/24  12:26 
# tool：PyCharm

import requests
def getHTMLText(url,header):
    try:
        response = requests.get(url,headers=header,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        return response.text[:1000]
    except:
        return '产生异常'
if __name__ == '__main__':
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    url = 'https://item.jd.com/100010393763.html'
    print(getHTMLText(url,headers))