# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/23  16:53 
# tool：PyCharm

import json
# urllib下的request,用来发起HTTP请求
import urllib.request

#指定http版本
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


# url为获取github中的第一页Python项目数据的请求url
url = 'https://api.github.com/search/repositories?q=language:python&page=1'
with urllib.request.urlopen(url) as response:
    # response对象的read方法返回的是一个字节流对象，需通过decode方法进行解码
    # 解码后的对象是一个JSON格式的字符串
    json_str = response.read().decode('utf-8')
    # 执行json模块的loads方法对JSON字符串进行反序列化
    repositories = json.loads(json_str)
    # 输出第一个Python仓库的信息
    print(repositories["items"][0])
