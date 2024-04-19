# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class Music163Pipeline:
    def open_spider(self, spider):
        self.f = open(r'D:\A\python\scrapyprojects\music163\data.csv', encoding='utf-8-sig', newline='', mode='w')
        self.csv_writer = csv.writer(self.f)
        self.csv_writer.writerow(['用户名', '时间', '点赞数', 'ip地址', '内容', '客户端'])

    def process_item(self, item, spider):
        nickname = item.get('nickname')
        time = item.get('time')
        likedCount = item.get('likedCount')
        ipLocation = item.get('ipLocation')
        content = item.get('content')
        OS_TYPE = item.get('OS_TYPE')
        data_list = [nickname, time, likedCount, ipLocation, content, OS_TYPE]
        self.csv_writer.writerow(data_list)
        print(data_list, '保存成功')


    def close_spider(self, spider):
        self.f.close()