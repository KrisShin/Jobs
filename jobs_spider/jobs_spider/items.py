# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    salary = scrapy.Field()
    position = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    company = scrapy.Field()
    category = scrapy.Field()
    people_num = scrapy.Field()
    date = scrapy.Field()
