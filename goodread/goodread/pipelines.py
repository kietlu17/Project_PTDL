# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv

class JsonDBBookPipeline:
    def process_item(self, item, spider):
        with open('jsondataunitop.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(line)
        return item

class CSVDBBookPipeline:
    '''
    mỗi thông tin cách nhau với dấu $
    Ví dụ: coursename$lecturer$intro$describe$courseUrl
    Sau đó, cài đặt cấu hình để ưu tiên Pipline này đầu tiên
    '''
    def process_item(self, item, spider):
        with open('csvdataunitop.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter='$')
            writer.writerow([
                item['bookUrl'],
                item['number'],
                item['bookname'],
                item['author'],
                item['prices'],
                item['describe'],
                item['rating'],
                item['ratingcount'],
                item['reviews'],
                item['fivestars'],
                item['fourstars'],
                item['threestars'],
                item['twostars'],
                item['onestar'],
                item['pages'],
                item['publish']
            ])
        return item
    pass

