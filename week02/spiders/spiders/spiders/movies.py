# -*- coding: utf-8 -*-
import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for movies in Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]:
            movie_name = movies.xpath('./div[1]/span[1]/text()').extract()[0]
            movie_type = movies.xpath('./div[2]/text()[2]').extract()[0].strip()
            release_time = movies.xpath('./div[4]/text()[2]').extract()[0].strip()

            content = SpidersItem()
            content['movie_name'] = movie_name
            content['movie_type'] = movie_type
            content['release_time'] = release_time

            yield content