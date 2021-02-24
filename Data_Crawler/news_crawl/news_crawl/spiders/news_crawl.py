import scrapy
import re
from datetime import datetime
import pandas as pd
from news_crawl.items import NewsCrawlItem

class CrawlNewsSpider(scrapy.Spider):
    name = 'news_crawl'
    url_format = "https://search.naver.com/search.naver?&where=news&query={0}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={1}&de={1}&docid=&nso=so:r,p:from{2}to{2},a:all&mynews=0&cluster_rank=34&start={3}"
            
    def __init__(
        self, keyword="", start="", end=""
        ):

        dot_start_date = start[:4] + '.' + start[4:6] + '.' + start[6:]
        dot_end_date = end[:4] + '.' + end[4:6] + '.' + end[6:]
        self.start_urls = [self.url_format.format(keyword, dot_start_date, start, 0)]

    def parse(self, response):
 
        for item in response.css("ul.list_news div.news_info div") :
            url = item.css("a::attr(href)")[1].get()
            print(url)
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):   
        item = NewsCrawlItem()

        item['url']=response.url
        item['title']=response.css("h3#articleTitle::text").get()
        item['media']=response.css("div.press_logo img::attr(title)").get()
        item['date']=response.css("div.sponsor span.t11::text").get()
        item['content']=''.join(response.css("div#articleBodyContents::text").getall()).replace("\n","").strip()

        yield item
