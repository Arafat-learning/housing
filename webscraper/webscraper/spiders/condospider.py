import scrapy
from webscraper.items import KrishaItem


class CondoSpider(scrapy.Spider):
    name = "condospider"
    allowed_domains = ["krisha.kz"]
    start_urls = ["https://krisha.kz/prodazha/kvartiry/astana/"]

    def parse(self, response):
        cards = response.css("div.a-card")

        for card in cards:

            card_item = KrishaItem()
            card_item["price"] = card.css("div.a-card__price::text").get()
            card_item["info"] = card.css("a.a-card__title::text").get()
            card_item["address"] = card.css("div.a-card__subtitle::text").get()
            card_item["description"] = card.css("div.a-card__text-preview::text").get()
            card_item["owner"] = card.css("div.a-card__owner").attrib["class"]
            card_item["category"] = "condominium"
            card_item["city"] = "Astana"

            yield card_item
