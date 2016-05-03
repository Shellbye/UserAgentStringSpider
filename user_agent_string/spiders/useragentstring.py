# -*- coding: utf-8 -*-
import scrapy

from ..items import UserAgentStringItem


class UseragentstringSpider(scrapy.Spider):
    name = "useragentstring"
    allowed_domains = ["useragentstring.com"]
    start_urls = (
        'http://www.useragentstring.com/pages/useragentstring.php',
    )

    def parse(self, response):
        urls = response.xpath("//table[@id='auswahl']/tr[1]/td[2]/a[@class='unterMenuName']/@href").extract()
        for url in urls:
            u = "http://www.useragentstring.com" + url
            yield scrapy.Request(url=u.strip(), callback=self.go_to_page)

    def go_to_page(self, response):
        strings = response.xpath('//*[@id="liste"]/ul/li/a/text()').extract()
        for string in strings:
            item = UserAgentStringItem()
            item['name'] = string
            yield item
