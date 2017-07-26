# -*- coding:utf-8 -*-

import urllib2


class HtmlDownloader(object):
    def download_html(self, host, url):
        if url is None or host is None:
            print 'url is null'
            return

        request = urllib2.Request(url)
        request.add_header('Referer', host)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        try:
            response = urllib2.urlopen(request, timeout=5)
            response_code = response.getcode()
            if 200 != response_code:
                print "URL : %s error_code: %d" % (url, response_code)
                return None
            return response.read().decode('utf-8')

        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                print "Url: %s\t%s" % (url, e.code)
            elif hasattr(e, 'reason'):
                print "Url: %s\t%s" % (url, 'error')

        finally:
            if response:
                response.close()


if __name__ == '__main__':
    h_download = HtmlDownloader()
    html = h_download.download_html("https://baike.baidu.com", "https://baike.baidu.com/view/2.htm")
    print html
