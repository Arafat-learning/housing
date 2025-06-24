import scrapy


class CondospiderSpider(scrapy.Spider):
    name = "condospider"
    allowed_domains = ["krisha.kz"]
    start_urls = ["https://krisha.kz/prodazha/kvartiry/astana/"]

    def parse(self, response):
        pass
