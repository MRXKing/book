# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem

#爬取小说阅读网的免费玄幻小说(信息)
class GetbookinfoSpider(scrapy.Spider):
    name = 'getbookinfo'
    allowed_domains = ['www.readnovel.com']
    pageNum = 1
    baseURL = 'https://www.readnovel.com/finish?pageSize=10&gender=1&catId=20001&isFinish=1&isVip=1&size=-1&updT=-1&orderBy=0&pageNum='
    start_urls = [baseURL + str(pageNum)]

    def parse(self, response):
        try:

            node_list = response.xpath("//div[@class='book-info']")

            for node in node_list:

                item = BookItem()

                item['book_name'] = node.xpath("./h3/a/text()").extract()[0]

                item['book_type'] = node.xpath("./p[1]/span[1]/text()").extract()[0]

                item['book_stat'] = node.xpath("./p[1]/span[2]/text()").extract()[0]

                item['book_author'] = node.xpath("./p[1]/span[3]/text()").extract()[0]

                yield item

            if self.pageNum != 16:
                self.pageNum += 1
                yield scrapy.Request(self.baseURL + str(self.pageNum), callback=self.parse)
        except Exception as e:
            print(e)
