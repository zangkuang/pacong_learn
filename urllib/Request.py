# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/28  20:39 
# tool：PyCharm

# 导入urllib库
import urllib.request

"""
# 向指定的url发送请求，并返回服务器响应的类文件对象
url = "http://www.baidu.com"
response = urllib.request.urlopen(url=url)
print(type(response))

# 类文件对象支持文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()
# html = response.readline() # 读取一行
# html = response.readlines() # 读取多行，返回列表
# 打印响应结果（byte类型）
# print(html)
# 打印响应结果（utf-8类型）
# 二进制和字符串之间的相互转码使用 encode() 和 decode() 函数
# encode() 和 decode() 可带参数，不写默认utf-8，其他不再特别说明
print(html.decode())
# 打印状态码
# print(response.get_code())
print(response.status)
# 获取响应头
print(response.getheaders())
# 获取响应头Server信息
print(response.getheader('Server'))
# 获取响应结果原因
print(response.reason)
"""

# 导入urllib库
import urllib.parse
import urllib.request

# 向指定的url发送请求，并返回
post_url = 'https://fanyi.baidu.com/sug'
# 传入参数
form_data = {
    'kw': 'honey'
}
# 格式化参数
form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(url=post_url, data=form_data)
# 打印服务器响应的类文件对象
print(type(response))

# 类文件对象支持文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()
# 打印响应结果（byte类型）
print(html)
# 打印响应结果（utf-8类型）
print(html.decode())
# 打印状态码
print(response.status)
# print(response.getcode())
# 获取响应头
print(response.getheaders())
# 获取响应头Server信息
print(response.getheader('Server'))
# 获取响应结果原因
print(response.reason)
