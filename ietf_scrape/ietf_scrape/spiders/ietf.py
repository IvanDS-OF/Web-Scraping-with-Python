import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]



    def parse(self, response):
        return {
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(), 
            'title': response.xpath('//span[@name="DC.Title"]/@content').get(), 
            'date': response.xpath('//span[@class="date"]/text()').get(),
            'description': response.xpath('@meta[@name="DC.Description.Abstract"]/@content').get(), 
            'author': response.xpath('//meta[@name="DC.Creator"]@ontent').get(), 
            'company': response.xpath('//span[@class="author_company"]/text()').get(), 
            'address': response.xpath('//span[@class="address"]/text()').get(), 
            'text': w3lib.html.remove.tags(response.xpath('//div[@class="text"]').get()), 
            'headings': response.xpath('//span[@@class="subheading"]/text').get()
        }



    def parse0(self, response):
        #To start with the project we can call the title of the page, so we need to go to the Source page
        #and find the  <span class="title">A Standard for the Transmission of IP Datagrams on Avian Carriers</span>
        #It is gonna be in HTML, so, once identified, we have 3 options to obtain this information from the page
        #The first one is using CSS, as follow
        #title = response.css('span.title::text'.get())
        #and the other one is using xpath
        title = response.xpath('//span[@class="title"]/text()').get()

        return { #We must to return a dictinary
            "title": title
        }

        #Then, to run this file properly, we need to use a scrapy command, the follow one
        #$ scrapy runspider ietf.py

        #This command returns all the values found, we must filter the information although

        #pass


        
