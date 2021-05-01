import requests
import time
from multiprocessing import Queue
from threading import Thread
import json
import urllib.parse     #用于解析url

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?'
        self.headers = {'User-Agent': 'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()

    # URL入队列
    def getUrl(self):
        # 生成50个URL地址,放到队列中
        for page in range(50):
            params = {
                'page': str(page),
                'categoryId' : '2',
                'pageSize' : '30'
            }
            #进行编码
            params = urllib.parse.urlencode(params)
            # 把拼接的url放到url队列中
            fullurl = self.url + params
            # print(fullurl)
            self.urlQueue.put(fullurl)

    # 采集线程事件函数,发请求,把html给解析队列
    def getHtml(self):
        while True:
            # 如果队列不为空,则获取url
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                res = requests.get(url,headers=self.headers)
                html = res.text
                #content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
                # 把html发到解析队列
                self.parseQueue.put(html)
            else:
                break

    # 解析线程事件函数,从解析队列get,提取并处理数据
    def parseHtml(self):
        while True:
            # 把html转换成json格式
            try:
                html = self.parseQueue.get(block=True,timeout=2)
                # print(html)
                #阻塞，等待2秒
                hList = json.loads(html)['data']
                print(hList)
                # hList : [{应用信息1},{},{}]
                for h in hList:
                    # 应用名称
                    name = h['displayName']
                    # 应用链接
                    d = {
                        '应用名称' : name.strip(),
                        '应用链接' : 'http://app.mi.com/details?' + h['packageName']
                    }
                    with open('xiaomi.json','a') as f:
                        f.write(str(d) + '\n')
            except:
                break


    # 主函数
    def workOn(self):
        # url入队列
        self.getUrl()
        # 存放所有采集线程对象的列表
        tList = []
        # 采集线程开始执行
        # for i in range(1):        #非多线程
        for i in range(6):
            t = Thread(target=self.getHtml)     #
            tList.append(t)
            t.start()
        # 解析线程开始执行
        # for i in range(1):
        for i in range(6):
            t = Thread(target=self.parseHtml)
            tList.append(t)
            t.start()
        # 统一回收解析线程
        for i in tList:
            i.join()

if __name__ == '__main__':
    begin = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print('执行时间:%.2f' % (end-begin))
