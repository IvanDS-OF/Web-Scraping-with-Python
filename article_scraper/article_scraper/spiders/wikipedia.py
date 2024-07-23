import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from article_crawler.items import Article
from article_scraper.items import Article



class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]


    #Lets to define th object of the rules, The rules are lists
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]
    #This means that each time it finds an interla URL it follows that, then it keeps
    #following and following and finding new interal URLs 
    #LinkExtractor - Parses the HTML page and finds new Wiki links to visit 

    #If the name "parse" does ot work, change the name to "parse_info"
    def parse_info(self, response):
        #Start with defining what we want
        #Using Items, it is going to populate an article object
        #Instead to use a dictionary we will need the follow structure

        article = Article()
        
        article['title'] = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()')
        article['url'] = response.url
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
    
        #to run correctly the project modified with the articles and items it is necesary type the follow comand en CMD
        #$ scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10
        #           -o name of the new file -t the formar of the file -s Special requeriment (Close after 10 new pages)



