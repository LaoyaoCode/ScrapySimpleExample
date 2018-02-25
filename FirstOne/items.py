# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstoneItem(scrapy.Item):
    # define the fields for your item here like:
    index = scrapy.Field() #索引，用于顺序排列
    chapterName = scrapy.Field() #章节名字
    chapterWords = scrapy.Field() #章节内容
