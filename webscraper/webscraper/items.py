# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KrishaItem(scrapy.Item):
    price = scrapy.Field()
    info = scrapy.Field()
    room_count = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    owner = scrapy.Field()
    category = scrapy.Field()
    city = scrapy.Field()
