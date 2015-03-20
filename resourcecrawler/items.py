from scrapy.item import Item, Field

class ResourceItem(Item):
    url = Field()
    mimetype = Field()
    size = Field()
    referrer = Field()
