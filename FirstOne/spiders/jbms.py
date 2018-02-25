# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from FirstOne.items import FirstoneItem

class JbmsSpider(scrapy.Spider):
    name = 'jbms'
    start_urls = ['https://www.88dushu.com/xiaoshuo/41/41976/']
    base_url = 'https://www.88dushu.com/xiaoshuo/41/41976/'
    urlOrder = []

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")

        linkList = soup.find("div", {"class": "mulu"}).find("ul") #获取列表

        for li in linkList.findAll("li"):
            link = self.base_url + li.find("a")['href'] #获取每一章节的链接
            self.urlOrder.append(link)#将url按照顺序放在列表中
            yield scrapy.Request(link, callback=self.wordHtmlParse) #发送请求，去解析每一章节

    def wordHtmlParse(self, response):
        soup = BeautifulSoup(response.body, "lxml")

        item = FirstoneItem()
        novelDiv = soup.find("div", {"class": "novel"})

        chapterName = novelDiv.find("h1").text #获取章节标题
        chapterWords = novelDiv.find("div", {"class": "yd_text2"}).text

        item["chapterWords"] = chapterWords.replace("\xa0", "")
        item["index"] = self.urlOrder.index(response.url)
        item["chapterName"] = chapterName

        yield item


