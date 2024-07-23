import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]


    #Lets to define th object of the rules, The rules are lists
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]
    #This means that each time it finds an interla URL it follows that, then it keeps
    #following and following and finding new interal URLs 
    #LinkExtractor - Parses the HTML page and finds new Wiki links to visit 

    def parse(self, response):
        #Start with defining what we want
        return {
            'tittle': response.xpath('//h1/text()').get or response.xpath('//h1/i/text()').get(),
            'url': response.url, 
            'last_edited': response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        }
        
