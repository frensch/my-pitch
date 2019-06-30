import logging
import scrapy
import string

class GetArtistis(scrapy.Spider):
    name = 'midworld'
    letters = []
    start_urls = []
    links = []

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('scrapy')
        logger.setLevel(logging.CRITICAL)
        self.letters = list(string.ascii_uppercase)
        #self.letters = ['A','G', 'Z']
        self.start_urls = ['http://www.midiworld.com/files/' + str(x) + '/all/' for x in self.letters]
        super().__init__(*args, **kwargs)
        print(self.start_urls)
        

    def parse(self, response):
        
        for element in response.css('#page table a'):
            # print (title.xpath('text()').get()) #::attr(href)
            GetArtistis.links.append((element.xpath('text()').get(), element.xpath('@href').get()))
            yield {'title': element.get()}

        #for next_page in response.css('a.next-posts-link'):
        #    yield response.follow(next_page, self.parse)


class GetMusics(scrapy.Spider):
    name = 'GetMusics'
    letters = []
    start_urls = []
    links = []

    def __init__(self, urls='', *args, **kwargs):
        logger = logging.getLogger('scrapy')
        logger.setLevel(logging.CRITICAL)
        self.start_urls = urls
        print(self.start_urls)
        super().__init__(*args, **kwargs)
        

    def parse(self, response):
        for element in response.css('#page ul li'):
            # print (title.xpath('text()').get()) #::attr(href)
            self.links.append((element.xpath('text()').get(), element.xpath('span/text()').get(), element.xpath('a/@href').get()))
            yield {'element': element.get()}