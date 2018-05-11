# -*- coding: UTF-8 -*-
import scrapy
import json
from scrapy_splash import SplashRequest

des3PsnId = 'UPQ2oUMJesA%3D'
pageNo = 1
authors = ''
time = ''
class ScholarmateSpider(scrapy.Spider):
    name = "scholarmate"

    start_urls = [
        "https://www.scholarmate.com/pubweb/outside/ajaxpublist?des3PsnId="+des3PsnId+"&page.pageNo="+str(pageNo)
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url=url, callback=self.parse, args={'wait': 1}, endpoint='render.html')

    def parse(self, response):

        """
        The lines below is a spider contract about https://www.scholarmate.com .
        """
        for quote in response.xpath('//div[@class="pub-idx__main"]'):
            author_arr = quote.xpath(
                './/div[@class="pub-idx__main_author dev_pub_author"]/text() | .//div[@class="pub-idx__main_author dev_pub_author"]/strong/text()').extract()
            global authors
            for author in author_arr:
                authors += author
            # print(authors)
            src_str = quote.xpath('.//div[@class="pub-idx__main_src dev_pub_src"]/text()').extract_first()
            src_arr = src_str.split('，') #中文逗号
            last_index = len(src_arr)
            years = src_arr[last_index-1]
            year = ''.join('.'.join(years.split('.')[::-1]).split()) #时间翻转去空格
            journal = src_arr[0]
            detail_url = quote.xpath('.//div[@class="pub-idx__main_title dev_pub_title"]/a/@href').extract_first()
            yield {
                'title': quote.xpath('.//div[@class="pub-idx__main_title dev_pub_title"]/a/text()').extract_first().strip(),
                'author': authors,
                # 'src': quote.xpath('.//div[@class="pub-idx__main_src dev_pub_src"]/text()').extract_first(),
                'year': year,
                'journal': journal,
                'authors_uniid': des3PsnId,
            }
            authors = ''
            if detail_url is not None:
                yield scrapy.Request(detail_url, callback=self.parse_paper_detail)

        global pageNo
        if(pageNo<2):
            pageNo += 1
            next_page_url = 'https://www.scholarmate.com/pubweb/outside/ajaxpublist?des3PsnId='+des3PsnId+'&page.pageNo='+str(
                pageNo)
            # print(next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))
    # 论文详情页爬虫
    def parse_paper_detail(self, response):
        for quote in response.xpath('//div[@class="detail-pub__box"]'):
            yield {
                'title2': quote.xpath('.//div[@class="detail-pub__title"]/text()').extract_first(),
                'abstract': quote.xpath('.//div[@class="detail-pub__abstract_content"]/text()').extract_first(),
                'keywords': quote.xpath('.//div[@class="detail-pub__keyword_content"]/span/text()').extract(),
            }
            # print(quote.xpath('.//div[@class="detail-pub__abstract_content"]/text()').extract_first())
# scrapy crawl scholarmate -o wangwanliang.json -s FEED_EXPORT_ENCODING=utf-8