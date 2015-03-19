from scrapy.item import Item, Field

class PageItem(Item):
    url = Field()
    title = Field()
    size = Field()
    referer = Field()
    newcookies = Field()
    body = Field()

class ResourceItem(Item):
    url = Field()
    mimetype = Field()
    #name = Field()
    #description = Field()
    #size = Field()
