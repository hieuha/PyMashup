import urllib2
import StringIO
import gzip


class MyBot(object):

    """docstring for MyBot"""

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
        self.cookie = ""
        self.header = {'User-Agent': self.user_agent}

    def get(self, url):
        req = urllib2.Request(url, headers=self.header)
        res = urllib2.urlopen(req)
        html = res.read()

        if res.info().get('Content-Encoding') == 'gzip':
            buf = StringIO.StringIO(html)
            f = gzip.GzipFile(fileobj=buf)
            html = f.read()
        return html

    def post(self, data):
        pass
