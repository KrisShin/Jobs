# -*- coding: utf-8 -*-
import scrapy


class LgSpiderSpider(scrapy.Spider):
    name = 'lg_spider'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/list_{key}?isSchoolJob=1']

    def parse(self, response):
        pass
