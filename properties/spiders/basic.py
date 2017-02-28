# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = ['https://www.gumtree.com/flats-houses']

    def parse(self, response):
        self.log("title: %s" % response.xpath(
        	'//*[contains(concat(" ", normalize-space(@class)," "), "listing-title")][1]/text()').extract())

        self.log("price: %s" % response.xpath(
        	'//*[contains(concat(" ", normalize-space(@class)," "), "listing-price")][1]/text()').re('[.0-9]+'))

        self.log("description: %s" % response.xpath(
        	'//*[contains(concat(" ", normalize-space(@class)," "), "listing-description")][1]/text()').extract())

        self.log("address: %s" % response.xpath(
        	'//*[contains(concat(" ", normalize-space(@class)," "), "listing-location")][1]/text()').extract())

        self.log("image_urls: %s" % response.xpath(
        	'//*[contains(concat(" ", normalize-space(@class)," "), "listing-link")][1]/text()').extract())