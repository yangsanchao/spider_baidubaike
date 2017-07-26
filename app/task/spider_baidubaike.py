# -*- coding:utf-8 -*-

import time
import MySQLdb
from app.common.html_download import HtmlDownloader
from app.common.html_parser import HtmlParser
from app.conf import conf


class SpiderBaiDuBaiKe(object):
    def __init__(self):
        self.download = HtmlDownloader()
        self.html_parser = HtmlParser()
        self.__downloading = False
        self.__host = "https://baike.baidu.com"
        self.__index = self.get_last_index()
        print "self.__index %d " % self.__index
        self.__mysql_buffer = []

    def get_last_index(self):
        try:
            conn = MySQLdb.connect(host=conf.DBHOST,
                                   port=3306,
                                   user=conf.DBUSER,
                                   passwd=conf.DBPWD,
                                   db=conf.DBNAME,
                                   charset='utf8')
            cursor = conn.cursor()
            cursor.execute("SELECT *FROM nlp.baidubaike order by id desc")
            data = cursor.fetchone()
            url = data[3]
            url_spilt = url.split("/")
            index = url_spilt[len(url_spilt) - 1].split(".")
            return int(index[0])
        except:
            return 0
        finally:
            conn.close()


    def start_spider(self):
        self.__downloading = True
        while self.__downloading:
            # self.__downloading = False
            URL = "https://baike.baidu.com/view/" + str(self.__index) + ".htm"
            self.spider_url(URL)
            time.sleep(1 / 10000)
            self.__index += 1

    def spider_url(self, url):
        try:
            html = self.download.download_html(self.__host, url)
            # print html
            title, tag = self.html_parser.parse_html(html)
            self.write_to_mysql(title, tag, url)

        except:
            # print '--- craw failed! ---'
            pass

    def write_to_mysql(self, title, tag, url):
        # print title, tag.replace("\n", ""), url
        self.__mysql_buffer.append((title, tag.replace("\n", ""), url))
        if len(self.__mysql_buffer) % 100 == 0:
            try:
                # print self.__mysql_buffer
                # write to mysql
                conn = MySQLdb.connect(host=conf.DBHOST,
                                       port=3306,
                                       user=conf.DBUSER,
                                       passwd=conf.DBPWD,
                                       db=conf.DBNAME,
                                       charset='utf8')
                # 使用cursor()方法获取操作游标
                cursor = conn.cursor()
                sql = "replace into nlp.baidubaike(vocabularyEntry,vocabularyEntryClass,url) values(%s,%s,%s)"
                cursor.executemany(sql, self.__mysql_buffer)
                conn.commit()

            except Exception as e:
                print "mysql insert error !! ", e
            finally:
                conn.close()
                self.__mysql_buffer = []


if __name__ == '__main__':
    s = SpiderBaiDuBaiKe()
    s.start_spider()
