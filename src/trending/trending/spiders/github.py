# -*- coding: utf-8 -*-
import scrapy
from trending.items import TrendingItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = [
        'https://github.com/showcases/programming-languages',
        'https://github.com/showcases/web-accessibility',
        'https://github.com/showcases/open-source-integrations',
        'https://github.com/showcases/text-editors',
        'https://github.com/showcases/devops-tools',
        'https://github.com/showcases/serverless-architecture',
        'https://github.com/showcases/productivity-tools',
        'https://github.com/showcases/projects-that-power-github',
        'https://github.com/showcases/data-visualization',
        'https://github.com/showcases/machine-learning',
        'https://github.com/showcases/nosql-databases'
    ]

    def parse(self, response):
        items = TrendingItem()

        selector_title = 'h1.f00-light.lh-condensed.mb-1::text'
        selector_links = '.repo-list-item .mb-1 a::attr(href)'

        elem_title = response.css(selector_title)
        elem_link = response.css(selector_links)

        items['title'] = elem_title.extract_first().strip()
        items['trending'] = elem_link.extract()

        yield items
