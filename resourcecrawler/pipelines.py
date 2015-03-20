import os
from scrapy import signals, log
from scrapy.contrib.exporter import CsvItemExporter

class CsvExportPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.filepath = os.path.abspath(spider.output_file)
        file = open(self.filepath, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()
        log.msg('CSV output file location: "%s"' % self.filepath)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
