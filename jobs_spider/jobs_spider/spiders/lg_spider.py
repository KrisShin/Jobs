# -*- coding: utf-8 -*-
import scrapy


class LgSpiderSpider(scrapy.Spider):
    name = 'lg_spider'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
