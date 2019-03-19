from crawl_txt.items import CrawlTxtItem

import scrapy

from random import randint

class CrawlTxt(scrapy.Spider):
    name='CT'
    UserAgent = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
        'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    ]
    def start_requests(self):
        self.url='https://www.booktxt.net/1_1722/'
        yield scrapy.Request(self.url,headers={'user-agent':self.UserAgent[0]})#callback=self.abc)
        
    def parse(self,response):
        x=response.xpath('//dl/dd')
        for i in range(len(x)):
            if i<=7:
                continue
            else:
                yield scrapy.Request(self.url+x[i].xpath('./a/@href').extract()[0],headers={'user-agent':self.UserAgent[0]},callback=self.parse_content,meta={'i':i,'cookiejar':randint(1,5)})
    def parse_content(self,response):
        item=CrawlTxtItem()
        item['title']=str(response.meta['i'])+response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        item['content']=''
        for i in response.xpath('//div[@id="content"]/text()').extract():
            item['content']+=i
            item['content']+='\n'
        #for i in response.xpath('//div[@id="content"]/text()'):
          #  item['content']+=i.text[24:]
          #  item['content']+='\n'
        yield item
