# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse_html(self, html):
        if html is None:
            print "html is None %s" % __file__
        bs4 = BeautifulSoup(html, 'html.parser')
        tag = ""
        title = ""
        title = self.get_title(bs4)
        tag = self.get_tag(bs4)
        return title, tag

    def get_title(self, soup):
        # 匹配<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>节点，获得title
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        # 获得title_node的文字信息
        title = title_node.get_text()
        return title

    def get_tag(self, soup):
        tag = ""
        tag_htmls = soup.find_all('span', class_='taglist')
        for tag_html in tag_htmls:
            tag = tag + tag_html.get_text() + " "

        return tag
