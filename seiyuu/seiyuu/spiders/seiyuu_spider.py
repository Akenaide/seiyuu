
import os

import scrapy
from scrapy import log

from seiyuu import settings
from seiyuu.items import SeiyuuItem
from seiyuu import tools

class SeiSpider(scrapy.Spider):
    name = "seiyuu"
    allowed_domain = "myanimelist.net"
    urls_path = os.path.join(settings.PROJECT_ROOT, "urls.txt")
    start_urls = list()

    if os.path.isfile(urls_path):
        urls = open(urls_path, 'rb').readlines()
        for url in urls:
            start_urls.append(tools.get_google_cache(url))
    else:
        raise OSError(urls_path, 'not found please create it')

    def parse(self, response):
        seiyuu = SeiyuuItem()
        anime_name = response.xpath('//div/h1/text()').extract()
        div = response.xpath("//table/tr").css("td:nth-child(2)").css("div:nth-child(3)")
        for table in div.xpath('.//table'):
            seiyuu['anime'] = anime_name[0]
            infos =  table.xpath(".//a/text()").extract()
            if len(infos) == 2:
                seiyuu['character'], seiyuu['name'] = infos
                yield seiyuu
