# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

class BookPipeline(object):

    def __init__(self):
        self.col = client['book']['bookinfo']

    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item

    def close_spider(self,spider):
        client.close()


class ContentPipeline(object):

    def process_item(self, item, spider):
        data = dict(item)
        col = client['book'][data['book_name']]
        data.pop('book_name')
        col.insert(data)
        return item
