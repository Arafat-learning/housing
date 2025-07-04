import scrapy
from webscraper.items import KrishaItem


class CondoSpider(scrapy.Spider):
    name = "condospider"
    allowed_domains = ["krisha.kz"]
    start_urls = ["https://krisha.kz/prodazha/kvartiry/astana/"]

    def parse(self, response):
        # card of condominium
        cards = response.css("div.a-card")

        for card in cards:

            # title with room number and area
            info = card.css("a.a-card__title::text").get()
            parsed_title = info.split(" · ")

            card_item = KrishaItem()
            card_item["price"] = card.css("div.a-card__price::text").get()
            card_item["info"] = info
            card_item["room_count"] = parsed_title[0]
            card_item["area"] = parsed_title[1]
            card_item["address"] = card.css("div.a-card__subtitle::text").get()
            card_item["description"] = card.css("div.a-card__text-preview::text").get()
            card_item["owner"] = card.css("div.a-card__owner").attrib["class"]
            card_item["category"] = "condominium"
            card_item["city"] = "Astana"

            # cards of newly building places lack floor info in title
            try:
                card_item["floor"] = parsed_title[2]
            except:
                card_item["floor"] = None

            yield card_item
