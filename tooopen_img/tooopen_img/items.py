# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TooopenImgItem(scrapy.Item):
    # define the fields for your item here like:
    # Primary fields
    category = scrapy.Field()
    image_urls = scrapy.Field()

    # Calculated fields
    images = scrapy.Field()
    location = scrapy.Field()

    # Housekeeping fields
    url = scrapy.Field()
    date = scrapy.Field()
