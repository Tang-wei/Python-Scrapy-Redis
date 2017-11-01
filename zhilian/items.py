# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    pay = scrapy.Field()
    site = scrapy.Field()
    times = scrapy.Field()
    gangwei = scrapy.Field()
    url = scrapy.Field()
    miaoshu = scrapy.Field()
    #crawled = scrapy.Field()
