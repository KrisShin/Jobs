# -*- coding: utf-8 -*-
import scrapy

from jobs_spider.items import JobsItem

key_word = 'Python'

class ZpSpiderSpider(scrapy.Spider):
    name = 'zp_spider'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query={key_word}&scity=101270100']

    def parse_job_list(self, response):
        jobs = response.selector.css('#main > div > div.job-list > ul > li')
        for job in jobs:
            item = JobsItem()
