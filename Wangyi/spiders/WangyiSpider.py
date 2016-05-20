# -*- coding: utf-8 -*-
from scrapy.spiders import BaseSpider
from Wangyi.items import ArticleItem
from scrapy.http import Request
import json
import scrapy
class WangyiSpider(BaseSpider):
    name = 'Wangyi'
    allowed_domains = ['news.163.com']

    start_urls = [
            'http://news.163.com/index.html',
        ]


    def parse(self, response):
        urls = response.xpath('//a/@href').re(r'http://news.163.com/\d\d/\d{4}/\d\d/.+.html')
        for url in set(urls):
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        item =  ArticleItem()
        try:
            item['url'] = response.url
            item['title'] = response.xpath('//h1/text()').extract()[0]
            paras = response.xpath('//div[@id="endText"]//p').extract()
            item['content'] = ''.join(paras)
            paras = response.xpath('//div[@id="endText"]//text()').extract()
            item['raw'] = ''.join(paras)
            item['article_type'] = response.xpath('//div[@class="post_crumb"]//a/text()').extract()[2]
            item['author'] = response.xpath('//a[@id="ne_article_source"]/text()').extract()[0]
            item['source_link'] = response.xpath('//a[@id="ne_article_source"]/@href').extract()[0]
            item['publish_date'] = response.xpath('//div[@class="post_time_source"]/text()').re(r'\d{4}-\d\d-\d\d')[0]
            yield item
        except Exception as e:
            print "Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print e


        #print(item['title'])
        #print(item['content'])
