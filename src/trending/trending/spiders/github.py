# -*- coding: utf-8 -*-
import scrapy
from trending.items import TrendingItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    base_url = 'https://github.com'
    context = 'showcases'
    start_urls = [
        base_url + '/' + context + '/serverless-architecture',
        base_url + '/' + context + '/programming-languages',
        base_url + '/' + context + '/web-accessibility',
        base_url + '/' + context + '/open-source-integrations',
        base_url + '/' + context + '/text-editors',
        base_url + '/' + context + '/devops-tools',
        base_url + '/' + context + '/serverless-architecture',
        base_url + '/' + context + '/productivity-tools',
        base_url + '/' + context + '/projects-that-power-github',
        base_url + '/' + context + '/data-visualization',
        base_url + '/' + context + '/machine-learning',
        base_url + '/' + context + '/nosql-databases'
    ]

    def parse(self, response):
        items = TrendingItem()

        selector_title = 'h1.f00-light.lh-condensed.mb-1::text'
        selector_links = '.repo-list-item .mb-1 a::attr(href)'

        elem_title = response.css(selector_title)
        elem_link = response.css(selector_links)

        trending = []
        items['title'] = elem_title.extract_first().strip()
        for link in elem_link.extract():
            project_request = scrapy.Request(
                self.base_url + link,
                callback=self.parse_child,
                meta = {'item': items}
            )
            yield project_request
        yield items

    def parse_child(self, response):
        item = response.meta['item']
        selector_star = '.social-count.js-social-count::text'
        star = response.css(selector_star).extract_first().strip()
        project_page = []
        project_page.append(
            {
                'url': response.url,
                'star': star
            },
        )
        item['trending'] = project_page
        yield item

