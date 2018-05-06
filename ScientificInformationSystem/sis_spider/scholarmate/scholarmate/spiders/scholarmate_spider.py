# -*- coding: UTF-8 -*-
import scrapy
import json

class ScholarmateSpider(scrapy.Spider):
    name = "scholarmate"
    start_urls = [
        "https://www.scholarmate.com/P/zua2Y3?module=pub"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract about https://www.scholarmate.com .
        """

        print('res:',response.xpath('//div[@class="main-list"]'))
        for quote in response.xpath('//div[@class="pub-idx__main"]'):
            print('quote:', quote)
            yield {
                'title': quote.xpath('.//div[@class="pub-idx__main_box"]/div[@class="pub-idx__main_title"]/a/text()').extract_first(),
                'author': quote.xpath('.//div[@class="pub-idx__main_author dev_pub_author"]/text()').extract_first(),
                'src': quote.xpath('.//div[@class="pub-idx__main_src dev_pub_src"]/text()').extract_first()
            }
        # for url in response.xpath('//div[@class="list-wrap"]'):
        #     yield{
        #         print('url:::', url.xpath('//span/text()').extract_first())
        #     }

        next_page_url = response.xpath('//div[@class="pub-idx__main"]').extract_first()
        print('url:',next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


# scrapy crawl scholarmate -o items.json -s FEED_EXPORT_ENCODING=utf-8
