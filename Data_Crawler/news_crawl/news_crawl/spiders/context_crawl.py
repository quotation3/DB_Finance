import scrapy
import re
from datetime import datetime
import pandas as pd
from news_crawl.items import NewsCrawlItem

class CrawlNewsSpider(scrapy.Spider):
    name = 'context_crawl'

    def __init__(self, file):
        self.urls = list(pd.read_csv(file, header=None)[0])

    def start_requests(self) :
        for url in self.urls :
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = NewsCrawlItem()

        item['url']=response.url
        item['title']=response.css("h3#articleTitle::text").get()
        item['media']=response.css("div.press_logo img::attr(title)").get()
        item['date']=response.css("div.sponsor span.t11::text").get()
        item['content']=''.join(response.css("div#articleBodyContents::text").getall()).replace("\n","").strip()

        yield item
