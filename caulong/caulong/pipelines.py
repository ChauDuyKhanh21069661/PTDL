# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import pymongo
import json
# from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv
import os


class MongoDBCauLongPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://192.168.11.164:27017')
        self.db = self.client['dbcaulong'] #Create Database      
        pass
    def process_item(self, item, spider):
        
        collection =self.db['tblcaulong'] #Create Collection or Table
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")       
        pass
class JsonDBCauLongPipeline:
    def process_item(self, item, spider):
        with open('caulong.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(line)
        return item

class CSVDBCauLongPipeline:
    def process_item(self, item, spider):
        with open('caulong.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([
                item['ma'],
                item['tensp'],
                item['gia'],
                item['thuongHieu'],
                item['tinhTrang'],
                item['trinhDo'],
                item['noiDung'],
                item['phongCach'],
                item['doCung'],
                item['diemCanBang'],
                item['trongLuong'],
                item['thongTin']
            ])
        return item
    pass
