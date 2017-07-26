# -*- coding:utf-8 -*-
from app.task.spider_baidubaike import SpiderBaiDuBaiKe


class Spider(object):
    def __init__(self):
        self.spider_baidubaike = SpiderBaiDuBaiKe()

    def start(self):
        self.spider_baidubaike.start_spider()


if __name__ == '__main__':
    s = Spider()
    s.start()
