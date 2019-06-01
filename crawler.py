import scrapy
import re

class ArticleScraper(scrapy.Spider):
    name = "article"
    start_urls = [
        'https://www.npr.org/2019/06/01/728903700/what-we-know-about-the-virginia-beach-mass-shooting-victims',
    ]

    def parse(self, response):
        for link in response.css('a'):
            # only if the link is off-site
            url = link.css('a ::attr(href)').get()
            print(response.url)
            isSiteLink = False
            responseDomain = re.findall('\.(.*)\..*',response.url)[0]
            if url is not None:
                urlDomainMatched = re.findall('\.(.*)\..*',url)
                isSiteLink = re.match('/.*', url)
                if len(urlDomainMatched) == 1:
                    isSiteLink = (responseDomain == urlDomainMatched[0])
            if not isSiteLink:
                yield {
                    'text': link.css('a ::text').get(),
                    'url': url,
                }