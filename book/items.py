# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#书籍信息的字段
class BookItem(scrapy.Item):
    # define the fields for your item here like:

    #书籍名称
    book_name = scrapy.Field()

    #书籍类型
    book_type = scrapy.Field()

    #书籍状态  例如:已完结
    book_stat = scrapy.Field()

    #书籍作者
    book_author = scrapy.Field()

    #书籍字数
    book_fontNum = scrapy.Field()

#书籍内容的字段
class ContentItem(scrapy.Item):

    #章节标题
    book_chapter_titile = scrapy.Field()

    #章节内容
    book_chapter_content = scrapy.Field()

    #库名
    book_name = scrapy.Field()



