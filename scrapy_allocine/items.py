# -*- coding: utf-8 -*-

import scrapy

class Movie(scrapy.Item):
    name = scrapy.Field()
    press_rated = scrapy.Field()
    users_rated = scrapy.Field()
    short_description = scrapy.Field()
