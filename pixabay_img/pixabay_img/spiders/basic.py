# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
# from scrapy.loader.processors import Join, MapCompose
from scrapy.spiders import CrawlSpider, Rule

from pixabay_img.items import PixabayImgItem


class BasicSpider(CrawlSpider):
    name = 'basic'
    allowed_domains = ['pixabay.com']
    start_urls = ['https://pixabay.com/en/photos/nature/']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='//*[contains(@class, "pure-button")][2]/@href')),
        Rule(LinkExtractor(
            restrict_xpaths='//*[contains(@class, "item")]'), callback='parse_item')
    )

    def parse_item(self, response):
        # Create the loader using the selector
        l = ItemLoader(item=PixabayImgItem(), response=response)

        # Load fields using XPath expressions
        # To be finished by parsing .jpg element
        # l.add_xpath('field1', xpath2)
        # l.add_xpath('field2', xpath2)

        return l.load_item()
