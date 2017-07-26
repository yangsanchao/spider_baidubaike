# -*- coding:utf-8 -*-

from app.task.spider_baidubaike import SpiderBaiDuBaiKe

__author__ = 'yangsanchao'
__version__ = '1.0'
__date__ = '2017/06/28 12:24'

if __name__ == '__main__':
    print "running!!!"
    s = SpiderBaiDuBaiKe()
    s.start_spider()
