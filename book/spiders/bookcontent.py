# -*- coding: utf-8 -*-
import scrapy
from book.items import ContentItem

#爬取小说阅读网的免费武侠小说(内容)
class BookcontentSpider(scrapy.Spider):

    name = 'bookcontent'
    allowed_domains = ['www.readnovel.com']
    pageNum = 1
    baseURL = 'https://www.readnovel.com/finish?pageSize=10&gender=1&catId=20010&isFinish=1&isVip=1&size=6&updT=-1&orderBy=0&pageNum='
    start_urls = [baseURL+str(pageNum)]
    prefix = 'https://www.readnovel.com'

    def parse(self, response):
            node_list = response.xpath("//div[@class='book-info']")

            for node in node_list:

                item = ContentItem()

                item['book_name'] = node.xpath("./h3/a/text()").extract()[0]

                yield scrapy.Request(self.prefix + node.xpath("./h3/a/@href").extract()[0], meta={'item': item}, callback=self.go)

            if self.pageNum != 16:
                self.pageNum += 1
                yield scrapy.Request(self.baseURL + str(self.pageNum), callback=self.parse)

    def go(self, response):
        yield scrapy.Request("https://"+response.xpath("//a[@class = 'pink-btn J-getJumpUrl ']/@href").extract()[0], meta={'item': response.meta['item']}, callback=self.getContent)

    def getContent(self, response):

        item = response.meta['item']

        item['book_chapter_titile'] = response.xpath("//div[@class='main-text-wrap']/div[1]/h3/text()").extract()[0]

        item['book_chapter_content'] = response.xpath("normalize-space(string(//div[@class='main-text-wrap']/div[2]))").extract()[0].replace(u'\u3000', '')

        yield item

        if response.xpath("//a[@id='j_chapterNext']/text()").extract()[0] != "书末页":
            yield scrapy.Request("https://"+response.xpath("//a[@id='j_chapterNext']/@href").extract()[0], meta={'item': item}, callback=self.getContent)


