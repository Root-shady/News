# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import MySQLdb
#from twisted.enterprise import adbapi
from scrapy.pipelines.images import ImagesPipeline


class WangyiPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
    """
    A pipeline to store the item in a MySQL database
    """
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        dbargs = dict(
                host = settings['MYSQL_HOST'],
                db = settings['MYSQL_DBNAME'],
                user = settings['MYSQL_USER'],
                passwd = settings['MYSQL_PASSWD'],
                charset = 'utf8',
                use_unicode = True
            )
        conn = MySQLdb.connect(**dbargs)
        return cls(conn)


    def __init__(self, conn):
        #self.conn = MySQLdb.connect(user='root', passwd = '6566619', db = 'project',
        #       host='localhost', charset='utf8', use_unicode=True,)
        self.conn = conn
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print(type(item['title']))
        try:
#            sql = 'INSERT INTO article_article VALUES(null, "%s", "%s", "%s", "%s", "%s", "%s");'%(item['title'].encode('utf-8'), item['content'].encode('utf-8'), item['author'].encode('utf-8'), item['source_link'].encode('utf-8'), item['publish_date'].encode('utf-8'), item['url'].encode('utf-8'))
            sql = "INSERT INTO article_article VALUES(null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(item['title'].encode('utf-8'), item['content'].encode('utf-8'),item['author'].encode('utf-8'), item['source_link'].encode('utf-8'), item['publish_date'].encode('utf-8'), item['url'].encode('utf-8'), item['article_type'].encode('utf-8'), item['raw'].encode('utf-8'))
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            print("Error while insert into database", e)
        return item

    def close_spider(self, spider):
        self.conn.close()


#class ImageStorePipeline(ImagesPipeline):
#    def set_filename(self, response):
#        # instead of using the SHA1, use the md5 as required
#        # Return the image file name, use the md5 value of the given url
#        return 'full/{0}.jpg'.format(hashlib.md5(response.url).hexdigest())
#
#    def get_media_requests(self, item, info):
#        for image_url in item['image_urls']:
#            yield scrapy.Request(image_url)
#    def get_images(self, response, request, info):
#        for key, image, buf in super(ImageStorePipeline, self).get_images(response, request, info):
#            key = self.set_filename(response)
#        yield key, image, buf
