# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstonePipeline(object):

    wordsDic = {} #保存文字的字典
    indexList = [] #保存索引的列表

    def process_item(self, item, spider):

        self.indexList.append(item["index"])
        self.wordsDic[str(item["index"])] = item["chapterName"] + "\n" +  item["chapterWords"]
        return item

    def open_spider(self, spider):
        self.file = open("鉴宝秘术.txt", "w", encoding='utf-8') #覆盖原有文件
        print("spider start")

    def close_spider(self, spider):
        self.indexList.sort() #列表排序

        for index in self.indexList: #按照顺序写入文件
            self.file.write(self.wordsDic[str(index)])

        self.file.close()
        print("spider close")


