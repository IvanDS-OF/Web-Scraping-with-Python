import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
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
