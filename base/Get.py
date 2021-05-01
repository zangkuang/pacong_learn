# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/22  19:32 
# tool：PyCharm
import requests

#get
"""URL = "http://chipscoco.com/?id=9"
response = requests.get(URL)

# http状态码为200，说明请求成功
if response.status_code == 200:
    # 输出http服务器的响应头
    print(response.headers)
    # 输出字符串类型的响应体
    print(response.text)
# help(requests.get)"""

#post
URL = "https://passport.jd.com/new/login.aspx"

"""
(1) 定义一个全局的data对象，用来传递登录请求所需传递的参数
(2) 京东商城PC页面的登录远不止这些参数，而且涉及到参数的加密，在本节的代码中，仅演示如何发起POST请求，
     在后续的教程中会详细讲解如何模拟站点登录
"""

data = {
    "uuid": "7c52477f-66af-4902-8429-51d51f6b38c4",
    "loginname": "18819353206",
    "nloginpwd": "Thvm9iAfZ/MhW8VbEDSscBJtwxLLXCKki4g="
}

# 发起POST请求，参数data用来传递请求参数
response = requests.post(URL, data)
print(response.headers)
print(response.text)
# 登录失败，代码实例仅演示如何发起POST请求

'''
#text和content的区别
#.text（存的根据Beautifulsoup根据猜测的编码方式将content内容编码成字符串）是现成的字符串，.content(存的是字节码)还要编码
import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.baidu.com')
re_txt = response.text
re_content = response.content
print(re_txt)
print(type(re_txt))
print(re_content)
print(type(re_content))
response.encoding = 'utf-8'
re_txt = response.text
print(re_txt)
'''