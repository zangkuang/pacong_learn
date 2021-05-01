"""import requests
url = 'https://y.gtimg.cn/music/portal/js/v4/singerlist_9fd3b1e.js?max_age=31536000'
response=requests.get(url)
response.encoding='utf-8'
html=response.text
print(html)"""

import jsonpath
import json
import requests
import csv
import time
def writecsv(content):
	with open('spider2.csv','a+',encoding='utf-8',newline='') as filecsv:
		writer = csv.writer(filecsv)
		writer.writerow(content)
writecsv(['歌手名','歌手地区','歌手id','歌手图片'])
def getHtml(url):
	response=requests.get(url)
	response.encoding='utf-8'
	html=response.text
	html=json.loads(html)		#网页数据保存为json格式然后通过jsonpath解析json文件
	print(html)
	singname=jsonpath.jsonpath(html,'$..singerList..singer_name')
	# print(singname)
	singcountry=jsonpath.jsonpath(html,'$..singerList..country')
	# print(singcountry)
	singer_mid=jsonpath.jsonpath(html,'$..singerList..singer_mid')

	singer_pic=jsonpath.jsonpath(html,'$..singerList..singer_pic')
	# print(singer_mid)
	for index,i in enumerate(singname):
		writecsv([i,singcountry[index],singer_mid[index],singer_pic[index]])
index=0
for i in range(0,801,80):
	index=index+1
	getHtml('https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI01616088836276819&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"comm":{"ct":24,"cv":0},"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":%(no)d,"cur_page":%(page)d}}}'% {'no':i,'page':index})
	time.sleep(3)