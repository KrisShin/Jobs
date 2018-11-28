# -*- coding: utf-8 -*-
import scrapy


class BsSpiderSpider(scrapy.Spider):
    name = 'bs_spider'
    allowed_domains = ['zhipin.com']
    start_urls = ['http://https://www.zhipin.com/job_detail//']

    def search_parse(self, response):
        pass
