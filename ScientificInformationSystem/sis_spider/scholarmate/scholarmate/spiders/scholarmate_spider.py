# -*- coding: UTF-8 -*-
import scrapy
import json
from scrapy_splash import SplashRequest

class ScholarmateSpider(scrapy.Spider):
    name = "scholarmate"
    start_urls = [
        "https://www.scholarmate.com/pubweb/outside/ajaxpublist?des3PsnId=UPQ2oUMJesA%3D&page.pageNo=4"
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url=url, callback=self.parse, args={'wait': 1}, endpoint='render.html')

    def parse(self, response):
        """
        The lines below is a spider contract about https://www.scholarmate.com .
        """
        # print("PARSED", response.real_url, response.url)
        # print(response.xpath('//div[@class="pub-idx__main"]').extract())
        # print('res:',response.xpath('//div[@contains(@class,"main-list__item dev_pub_list_div")]'))
        for quote in response.xpath('//div[@class="pub-idx__main"]'):
            # print('quote:', quote)
            yield {
                'title': quote.xpath('.//div[@class="pub-idx__main_title dev_pub_title"]/a/text()').extract_first(),
                'author': quote.xpath('.//div[@class="pub-idx__main_author dev_pub_author"]/text()').extract_first(),
                'src': quote.xpath('.//div[@class="pub-idx__main_src dev_pub_src"]/text()').extract_first()
            }
        # for url in response.xpath('//div[@class="list-wrap"]'):
        #     yield{
        #         print('url:::', url.xpath('//span/text()').extract_first())
        #     }

        # next_page_url = response.xpath('//div[@class="pub-idx__main"]').extract_first()
        # print('url:',next_page_url)
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))


# scrapy crawl scholarmate -o items.json -s FEED_EXPORT_ENCODING=utf-8
