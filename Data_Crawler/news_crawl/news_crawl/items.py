# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsCrawlItem(scrapy.Item):
    title = scrapy.Field()
    media = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
