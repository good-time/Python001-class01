# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pretty_errors
from twisted.enterprise import adbapi 

class SpidersPipeline:
    def __init__(self,db_pool):
        self.db_pool = db_pool

    @classmethod  
    def from_settings(cls,settings):
        # 数据库初始化
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            database=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True 
        )

        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool)

    def process_item(self, item, spider):
        my_dict={}
        my_dict['name'] = item['movie_name']
        my_dict['types'] = item['movie_type']
        my_dict['release_time'] = item['release_time']

        query = self.db_pool.runInteraction(self.insert_sql, my_dict)
        query.addErrback(self.handle_error, my_dict, spider)
        return item


    def insert_sql(self,cursor,item):
        insert_sql = """insert into movies(name,types,release_time) values(%s,%s,%s)"""
        try:
            cursor.execute(insert_sql,(item['name'],item['types'],item['release_time']))
        except:
            print('插入数据出错')

    def handle_error(self, failure, item, spider):
        # #输出错误信息
        print("failure", failure)