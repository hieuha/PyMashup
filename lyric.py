import glob
import re


class Lyric(object):

    """docstring for Lyric"""

    def __init__(self, in_dir='output'):
        self.in_dir = in_dir
        self.lyrics = glob.glob(self.in_dir+'/*.lrc')

    def get_time(self, line):
        re_t = re.search(r'\[(.+?)\](.*)\[(.+?)\](.*)', line)
        return "%s %s\n" % (re_t.group(1), re_t.group(3))

    def search(self, pattern):
        f_w = open(self.in_dir+'/times.txt', 'w')
        for lyric in self.lyrics:
            print 'Processing %s' % lyric
            file_mp3 = lyric.replace('.lrc', '.mp3')
            with open(lyric, 'r') as f:
                for _ in xrange(7):  # Pass Header Zing
                    next(f)
                for line in f:
                    if pattern in line:
                        start = line.strip()
                        stop = f.next().strip()
                        line = '%s %s' % (start, stop)
                        f_w.write(file_mp3+'|'+self.get_time(line))
            f.close()
        f_w.close()
