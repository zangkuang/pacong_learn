# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
'''
用来存放爬虫怕写来的数据的模型
'''

class QsbkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义item数据字段
    author = scrapy.Field()
    content = scrapy.Field()
