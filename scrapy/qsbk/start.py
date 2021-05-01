# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/30  10:09
# tool：PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl qsbk_spider".split())

# execute里面需要传递列表数据，等价于
# cmdline.execute(["scrapy", "crawl", "qsbk_spider"])
