# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    raw = scrapy.Field()
    source_name = scrapy.Field()
    source_link = scrapy.Field()
    article_type = scrapy.Field()
    publish_date = scrapy.Field()
    author = scrapy.Field()
    click = scrapy.Field()
    comment = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()


