# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/25  10:28 
# tool：PyCharm

'''
输入：大学排名URL链接
输出：大学排名信息的屏幕输出（排名，大学名称，总分）
'''
import requests

def getHTMLText(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        response = response.json()      #使用json方法，将response对象转换为列表\字典
        return response
    except:
        return '产生异常'

#提取网页内容中信息到合适数据结构
def fillUnivList(result,data):
    true_data = data['data']['rankings']
    for item in true_data:
        ranking = item['ranking']
        name = item['univNameCn']
        score = item['score']
        college = {'排名':ranking,'名称':name,'评分':score}
        result.append(college)
    print(result)

if __name__ == '__main__':
    result = []
    url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2020'
    data = getHTMLText(url)
    fillUnivList(result,data)

