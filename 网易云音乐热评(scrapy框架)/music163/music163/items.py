# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Music163Item(scrapy.Item):
    nickname = scrapy.Field()
    time = scrapy.Field()
    likedCount = scrapy.Field()
    ipLocation = scrapy.Field()
    content = scrapy.Field()
    OS_TYPE = scrapy.Field()
