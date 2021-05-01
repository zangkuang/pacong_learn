import scrapy

from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        # SelectorList
        # 解析页面
        content_left = response.xpath('//div[@id="content-left"]/div')
        # 提取数据
        for dz_div in content_left:
            # Selector
            author = dz_div.xpath(".//h2/text()").get().strip()
            content_tmp = dz_div.xpath(".//div[@class='content']//text()").getall()
            content = ''.join(content_tmp).strip()
            item = QsbkItem(author=author, content=content)
            # 使用yield返回给pipeline
            yield item
