# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader

from pixabay_img.items import PixabayImgItem


class TooopenSpider(scrapy.Spider):
    name = 'tooopen'
    allowed_domains = ['tooopen.com']
    start_urls = ['http://www.tooopen.com/img/87.aspx']

    def parse(self, response):
        # Get the next index URLs and yield Requests
        for index in range(100):
            yield Request(f'http://www.tooopen.com/img/87_0_1_{index}.aspx')
        
        # Iterate through products and create PropertiesItems
        selectors = response.xpath('//*[contains(@class,"pic")]')
        for selector in selectors:
            yield self.parse_item(selector, response)

    def parse_item(self, selector, response):
        # Create the loader using the selector
        l = ItemLoader(item=PixabayImgItem(), selector=selector)

        # Load fields using XPath expressions
        l.add_xpath('category', './p[1]/text()')
        l.add_xpath('image_urls', './/@src')

        # Housekeeping fields
        l.add_xpath('url', './/@href')
        l.add_value('date', datetime.datetime.now())

        return l.load_item()
