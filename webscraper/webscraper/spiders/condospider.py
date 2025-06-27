import scrapy


class CondoSpider(scrapy.Spider):
    name = "condospider"
    allowed_domains = ["krisha.kz"]
    start_urls = ["https://krisha.kz/prodazha/kvartiry/astana/"]

    def parse(self, response):
        cards = response.css("div.a-card")

        for card in cards:
            yield {
            "price": card.css("div.a-card__price::text").get(),
            "info": card.css("a.a-card__title::text").get(),
            "address": card.css("div.a-card__subtitle::text").get(),
            "description": card.css("div.a-card__text-preview::text").get(),
            "owner": card.css("div.a-card__owner").attrib["class"]
            }
