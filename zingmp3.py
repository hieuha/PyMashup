import bot_request
from bs4 import BeautifulSoup
import re
import json
import StringIO


class ZingMp3(object):

    """docstring for ZingMp3"""

    def __init__(self):
        self.root_url = 'http://mp3.zing.vn/'
        self.bot = bot_request.MyBot()

    def top_song(self, limit=None):
        print 'Get Top VPOP'
        url_vn = 'http://mp3.zing.vn/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html'
        html = self.bot.get(url_vn)
        soup = BeautifulSoup(html, 'html.parser')
        table_song = soup.find('div', {'class': 'table-body'})
        songs_ul = table_song.ul.find_all('li')
        songs = []
        for i, song_li in enumerate(songs_ul):
            s_title, s_url = song_li.a.get('title'), song_li.a.get('href')
            songs.append((i, s_title, s_url))
        if limit:
            songs = songs[:limit]
        return songs

    def search(self, name):
        pass

    def song_info(self, song):
        info = tuple()
        root_info_url = 'http://mp3.zing.vn/html5xml/song-xml/'
        if song:
            i, s_title, s_url = song
            print 'Getting Information: %s' % s_title
            html = self.bot.get(s_url)
            re_p = re.search(r'xmlURL=(.+?)&amp;', html)
            # http://mp3.zing.vn/xml/song-xml/ZHxHykmNWzpGihDyLFctDHLn
            s_id = re_p.group(1).split('/')[-1]
            s_url_json = root_info_url+s_id
            json_data = self.bot.get(s_url_json)
            json_data = StringIO.StringIO(json_data)
            s_json = json.load(json_data)
            s_mp3_base = s_json['data'][0]['source_base']+'/'
            s_mp3 = s_mp3_base+s_json['data'][0]['source_list'][0]
            s_lyric = s_json['data'][0]['lyric']
            s_name = s_json['data'][0]['name']
            s_artist = s_json['data'][0]['artist']
            info = (s_name, s_artist, s_mp3, s_lyric)
        else:
            print 'Song is not exist'
        return info

    def songs_info(self, songs=[]):
        infos = list()
        if len(songs) > 0:
            for song in songs:
                info = self.song_info(song)
                infos.append(info)
        else:
            print 'The playlist is empty!'
        return infos
