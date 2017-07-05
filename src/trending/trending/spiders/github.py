# -*- coding: utf-8 -*-
import scrapy


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
        r = response.css('h1.f00-light.lh-condensed.mb-1::text')
        print(r.extract_first().strip())
