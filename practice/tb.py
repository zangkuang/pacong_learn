# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/27  12:33 
# tool：PyCharm
'''
需求：获取淘宝搜索页面的信息，提取其中的商品名称和价格
'''

import re
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
        cook = {'cookie': 'cookie2=1999d545702a200faef25bde551d0abe; t=68e184a2ed52c62af511bbd13c545239; _tb_token_=f3bfab75bd18b; cna=8x0EGWVCQ0ACAVmj3FKyKrqh; _samesite_flag_=true; xlly_s=1; _m_h5_tk=e7f3cff88e4d8e3e806e81dbc0ef1482_1619505413650; _m_h5_tk_enc=359519304ad731ae63a9f4a763ee7b25; sgcookie=E100se9FHndtGRffT7OCZuLNWwpjl%2BfmIrQjznvPdcPLidujRD3jMAoQbxqpSQz%2F48xLj2XQP%2BUv1YCtga0lStJxww%3D%3D; unb=2966584240; uc3=nk2=B0sXXZ0m0APbdThn&lg2=UtASsssmOIJ0bQ%3D%3D&id2=UUGk2KJkxHj5Yw%3D%3D&vt3=F8dCuwlHdRLjLWVA3NU%3D; csg=87eb44e4; lgc=dimusicmsjdj; cookie17=UUGk2KJkxHj5Yw%3D%3D; dnk=dimusicmsjdj; skt=df7f4e87b73b4375; existShop=MTYxOTQ5ODIxNw%3D%3D; uc4=id4=0%40U2OT6E24DsOaLLeOAYZlhAsDs2Th&nk4=0%40BQhejaHMWYATiweaZLRwIDqBtWkl8uI%3D; tracknick=dimusicmsjdj; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=j01; _nk_=dimusicmsjdj; cookie1=BdTjbx3dD58sLoxoBpfQuxafymhKeqfCFW0vKqQQEr0%3D; enc=qbQ1FaWVn1GOuXELYuiZj9NDOhibzr4K%2BX93y5W8wQCUjY63ZRoz1CQFh1SyB0syrZtVC3u6SX4ob%2BNaDf9BOg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci=24_1; alitrackid=tb.alicdn.com; lastalitrackid=tb.alicdn.com; JSESSIONID=07D64F84F5D347709089AB944E78E711; tfstk=c0vFBVVwKvHUze6SM96zAM8cjJjdasbllRSVtC8EUnkr88QhusV8yGvgkGSPkAfh.; l=eBND1jl4jXZ5pkLCBO5ahurza77OfIdbzsPzaNbMiInca1zN1LclENCCZvU6Rdtjgt5fFetPrUUpAdFWrR4LRA1Gi03HRs5mpeJ68e1..; isg=BPLyLC57xorDA_q2eP8hZF_8QzjUg_Yd4sSxi7zK8KXxT5BJpBZ8LUXlP-tzP261; uc1=cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie21=Vq8l%2BKCLjA%2Bl&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie14=Uoe1i6rVVACWDw%3D%3D&existShop=false&pas=0'}
        response = requests.get(url,headers = kv,cookie=cook,timeout=30)
        response.raise_for_status()     #如果状态不是200，引发HTTPError
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return '产生异常'



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}     #加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
data = {'log': '****',  #写入账户'pwd': '*****', #写入密码'wp-submit': '登录','redirect_to': 'https://w**','testcookie': '1'
}                                               #把有关登录的参数封装成字典，赋值给data。
login_in = requests.post(url,headers=headers,data=data)   #用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
cookies = login_in.cookies                      #提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'    #我们想要评论的文章网址。
data_1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'}                           #把有关评论的参数封装成字典。

comment = requests.post(url_1,headers=headers,data=data_1,cookies=cookies)   #用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
                                                 #调用cookies的方法就是在post请求中传入cookies=cookies的参数。
print(comment.status_code)                       #打印出comment的状态码，若状态码等于200，则证明我们评论成功。




def name_price(infolist,html):
    soup = BeautifulSoup(html,'html.parser')
    soup.find()

if __name__ == '__main__':

    goods = input('请输入你想查找的物品：')
    print(goods)
    infolist = []       #name和price存储
    start_url = 'https://s.taobao.com/search?q='+goods
    deepth = 2
    for i in range(deepth):
        try:
            url = start_url+'&s='+str(i*44)
            html = getHTMLText(url)
            print(html)
            name_price(infolist,html)
        except:
            continue
    print(infolist)
