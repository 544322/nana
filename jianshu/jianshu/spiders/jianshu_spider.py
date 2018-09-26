# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title=response.xpath("//h1[@class='title']/text()").get()
        avatar=response.xpath("//div[@class='author']/a[@class='avatar']/img/@src").get()
        author=response.xpath("//span[@class='name']/a/text()").get()
        pub_time=response.xpath("//span[@class='publish-time']/text()").get().replace("*","")
        url=response.url
        urli=url.split("?")[0]
        article_id=urli.split("/")[-1]
        content=response.xpath("//div[@class='show-content-free']").get()
        word_count=response.xpath("//span[@class='wordage']/text()").get()
        read_count=response.xpath("//span[@class='views-count']/text()").get()
        like_count=response.xpath("//span[@class='likes-count']/text()").get()
        comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        subjects=",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())


        item=JianshuItem(
            title=title,
            avatar=avatar,
            pub_time=pub_time,
            author=author,
            article_id=article_id,
            origin_url=response.url,
            content=content,
            read_count=read_count,
            like_count=like_count,
            subjects=subjects,
            word_count=word_count

        )
        yield item

