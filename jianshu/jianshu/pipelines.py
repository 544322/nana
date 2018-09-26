# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#数据导入到mysql中
import pymysql
#做数据库处理
from twisted.enterprise import adbapi
from pymysql import cursors

class JianshuPipeline(object):
    def __init__(self):
        dbparams={
            'host':'localhost',
            'user':'root',
            'port':3306,
            'password':'password',
            'database':'jianshu3',
            'charset':'utf8'
        }
        #host = 'localhost', user = 'root', password = 'password', database = 'pymysql_demo1', port = 3306
        self.conn=pymysql.connect(**dbparams)
        self.cursor=self.conn.cursor()
        self._sql=None


    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql="""
          insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values(null,%s,%s,%s,%s,%s,%s,%s)
            """
            return  self._sql
        return self._sql




class JianshutTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'user': 'root',
            'port': 3306,
            'password': 'password',
            'database': 'jianshu3',
            'charset': 'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

        @property
        def sql(self):
            if not self._sql:
                self._sql = """
                  insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values(null,%s,%s,%s,%s,%s,%s,%s)
                    """
                return self._sql
            return self._sql
        def process_item(self,item,spider):
            defer=self.dbpool.runInteraction(self.insert_item,item)
            defer.addErrback(self.handle_error,item,)


        def insert_item(self,cursor,item):
            cursor.exexute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))

        def handle_error(self,error,item,spider):
            print("="*10+"error"+'='*10)
            print(error)
            print('-'*10+"error"+'='*10)


