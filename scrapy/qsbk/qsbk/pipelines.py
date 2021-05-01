# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class QsbkPipeline(object):
    def __init__(self):
        """
        打开文件，也可放在open_spider中
        """
        self.fp = open('duanzi.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        """
        爬虫被打开的时候执行
        :param spider:
        :return:
        """
        print("爬虫开始....")

    def process_item(self, item, spider):
        """
        爬虫有item传过来的时候会被调用
        :param item:
        :param spider:
        :return:
        """
        item_json = json.dumps(dict(item), ensure_ascii=False)
        # 数据写入文件
        self.fp.write(item_json + '\n')
        return item

    def close_spider(self, spider):
        """
        爬虫关闭的时候被调用
        :param spider:
        :return:
        """
        # 关闭文件
        self.fp.close()
        print("爬虫结束....")
