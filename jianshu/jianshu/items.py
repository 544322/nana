# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    title=scrapy.Field()
    content=scrapy.Field()
    author=scrapy.Field()
    article_id=scrapy.Field()
    origin_url=scrapy.Field()
    avatar=scrapy.Field()
    pub_time=scrapy.Field()
    read_count=scrapy.Field()
    like_count=scrapy.Field()
    word_count=scrapy.Field()
    subjects=scrapy.Field()
    comment_count=scrapy.Field()

