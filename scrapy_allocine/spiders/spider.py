from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy_allocine.items import Movie

class AllocineSpider(CrawlSpider):
    name = 'allocine'
    allowed_domains = ['allocine.fr']
    start_urls = ['http://www.allocine.fr/film/meilleurs/', ]

    #rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@nav="pagination cf"]',)), callback="parse_query_page", follow= True),)
    rules = (Rule(
        LinkExtractor(restrict_css=('div.pagination-item-holder a')),
        follow=True,
        callback='parse_query_page',
    ),)

    # 
    def parsing(self, response):
        for bloc in response.css('.mdl'):
            yield {'name': bloc.css('h2.meta-title a ::text').extract_first(),}

    # recovers link
    def parse_query_page(self, response):
        links = response.css('h2.meta-title a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_movie_detail_page)

    # detail page
    def parse_movie_detail_page(self, response):
        movie = Movie()
        movie['name'] = response.xpath(
            '//div[contains(@class, "titlebar-title titlebar-title-lg")]/text()').extract_first().strip() or None

        movie['press_rated'] = response.xpath(
            '//span[contains(@class, "stareval-note")]/text()').extract()[0] or None

        movie['users_rated'] = response.xpath(
            '//span[contains(@class, "stareval-note")]/text()').extract()[1] or None

        movie['short_description'] = response.xpath(
            '//div[contains(@class, "content-txt ")]/text()').extract_first().strip() or None
        
        return movie