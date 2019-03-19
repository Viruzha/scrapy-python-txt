# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class CrawlTxtPipeline(object):
    def process_item(self, item, spider):
        with open(f'G:/python_学习/爬虫/scrapy/crawl_txt/txt/{item["title"]}.txt','w',encoding='utf8') as f:
            f.write(item['content'])        
        return item
