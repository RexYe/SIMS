# -*- coding: UTF-8 -*-
import scrapy
import json
from scrapy_splash import SplashRequest

des3PsnId = 'gdC9pv0cs%2BsWtCOpJd4RAg'
pageNo = 1
authors = ''
authors2 = ''
time = ''
key_words = ''
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
                'year': year,
                'journal': journal,
                'authors_uniid': des3PsnId.replace('%', ''),
            }
            authors = ''
            if detail_url is not None:
                yield scrapy.Request(detail_url, callback=self.parse_paper_detail)
        global pageNo
        if(pageNo<7):
            pageNo += 1
            next_page_url = 'https://www.scholarmate.com/pubweb/outside/ajaxpublist?des3PsnId='+des3PsnId+'&page.pageNo='+str(
                pageNo)
            # print(next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))
    # 论文详情页爬虫
    def parse_paper_detail(self, response):
        for quote in response.xpath('//div[@class="detail-pub__box"]'):
            author_arr2 = quote.xpath(
                './/div[@class="detail-pub__author"]/span/text() | .//div[@class="detail-pub__author"]/span/strong/text()').extract()
            global authors2
            set_of_authorarr = list(set(author_arr2)) #作者去重
            authors2=';'.join(set_of_authorarr)
            keywordsArr = quote.xpath('.//div[@class="detail-pub__keyword_content"]/span/text()').extract()
            global key_words
            key_words = ';'.join(keywordsArr)
            yield {
                'title2': quote.xpath('.//div[@class="detail-pub__title"]/text()').extract_first(),
                'author2': authors2,
                'abstract': quote.xpath('.//div[@class="detail-pub__abstract_content"]/text()').extract_first(),
                'key_words': key_words,
                'src': quote.xpath('.//div[@class="detail-pub__source"]/text()').extract_first(),
                'authors_uniid2': des3PsnId.replace('%', ''),
            }
            authors2 = ''
            # print(quote.xpath('.//div[@class="detail-pub__abstract_content"]/text()').extract_first())
# scrapy crawl scholarmate -o wangwanliang.json -s FEED_EXPORT_ENCODING=utf-8