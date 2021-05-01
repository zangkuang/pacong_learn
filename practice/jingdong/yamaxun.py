# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/24  12:40 
# tool：PyCharm

import requests
def getHTMLText(url):
    try:
        response = requests.get(url,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        return response.request.headers
    except:
        return '产生异常'
if __name__ == '__main__':
    url = 'https://www.amazon.cn/dp/B003L9T12A?ref_=Oct_DLandingS_D_50c96273_60&smid=A26HDXW89ZT98L'
    print(getHTMLText(url))
