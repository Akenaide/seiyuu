#!/usr/bin/env python
import os
import re

import scrapy
from scrapy import log

from crawl import settings
from crawl.items import SeiyuuItem
from crawl.items import CharacterItem
from crawl.items import AnimeItem
from crawl import tools

class SeiSpider(scrapy.Spider):
    name = "seiyuu"
    allowed_domain = "myanimelist.net"
    urls_path = os.path.join(settings.PROJECT_ROOT, "urls.txt")
    start_urls = list()
    base_url = "http://myanimelist.net"
    check_va_img = re.compile(r"voiceactors\/\d+\/.*")
    check_char_img = re.compile(r"characters\/\d+\/.*")

    check_people_link = re.compile(r"people\/\d+\/.*")
    check_char_link = re.compile(r"character\/\d+\/.*")
    check_anime_link = re.compile(r"anime\/\d+\/.*")

    if os.path.isfile(urls_path):
        urls = open(urls_path, 'rb').readlines()
        for url in urls:
            if url.strip():
                # start_urls.append(url.strip())
                start_urls.append(tools.get_google_cache(url.strip()))
    else:
        raise OSError(urls_path, 'not found please create it')

    def infos_from_a(self, a_tag):
        link = a_tag.xpath('@href').extract()[0]
        link = self.base_url + link
        text = a_tag.xpath('text()').extract()[0]
        return (link, text)

    def get_char_and_va_infos(self, table):
        seiyuu = dict()
        character = dict()
        imgs = table.xpath(".//img/@src").extract()
        for img in imgs:
            if self.check_va_img.search(img):
                seiyuu['image_link'] = img
            elif self.check_char_img.search(img):
                character['image_link'] = img

        infos = table.xpath(".//a[text()]")
        for info in infos:
            _dict = dict()
            _dict['page_link'], name = self.infos_from_a(info)
            if ',' in name:
                _dict['last_name'], _dict['first_name'] = name.split(',')
            else:
                _dict['last_name'] = name

            if self.check_char_link.search(_dict['page_link']):
                character.update(_dict)
            elif self.check_people_link.search(_dict['page_link']):
                seiyuu.update(_dict)

        return (character, seiyuu)

    def parse(self, response):
        seiyuu = SeiyuuItem()
        anime = AnimeItem()
        character = CharacterItem()

        anime['name'] = response.xpath('//div/h1/text()').extract()[0].strip()
        anime['start_time'] = response.xpath("//div[span/text()='Aired:']/text()").extract()[0]
        anime['page_link'] = response.url
        anime['image_link'] = response.xpath("//table/tr").css("td.borderClass").css("div:nth-child(1)").xpath(".//img/@src").extract()[0]
        yield anime
        div = response.xpath("//table/tr").css("td:nth-child(2)").css("div:nth-child(3)")
        for table in div.xpath(".//table[not(@class='space_table')]"):
            # if table.xpath("@class = 'space_table'").extract()[0] == '1':
            #     continue
            # seiyuu['anime'] = anime_name[0]
            # TODO handle no japanese seiyuu

            character_infos, seiyuu_infos = self.get_char_and_va_infos(table)
            seiyuu['page_link'] = seiyuu_infos.get('page_link', None)
            seiyuu['last_name'] = seiyuu_infos.get('last_name', "").strip()
            seiyuu['first_name'] = seiyuu_infos.get('first_name', "").strip()
            seiyuu['image_link'] = seiyuu_infos.get('image_link', None)
            yield seiyuu
            character['anime'] = anime
            character['seiyuu'] = seiyuu
            character['page_link'] = character_infos.get('page_link', None)
            character['last_name'] = character_infos.get('last_name', "").strip()
            character['first_name'] = character_infos.get('first_name', "").strip()
            character['image_link'] = character_infos.get('image_link', None)
            character['status'] = table.xpath(".//small/text()").extract()[0]
            yield character
