import multiprocessing
import os
import bot_request


class Download(object):

    """docstring for Download"""

    def __init__(self, songs, out_dir='output', number_thread=2):
        self.songs = songs
        self.q = multiprocessing.JoinableQueue()
        self.number_thread = number_thread
        self.out_dir = out_dir
        self.bot = bot_request.MyBot()
        if not os.path.isdir(out_dir):
            os.mkdir(self.out_dir)

    def download(self, url, file_name):
        raw = self.bot.get(url)
        f = open(self.out_dir+'/'+file_name, 'wb')
        f.write(raw)
        f.close()
        print 'Downloaded %s' % file_name

    def down_task(self, q):
        for song in iter(self.q.get, None):
            name, mp3, lyric = song[0], song[2], song[3]
            file_name = name.strip().replace(' ', '-')
            self.download(mp3, file_name+'.mp3')
            self.download(lyric, file_name+'.lrc')
            self.q.task_done()
        self.q.task_done()

    def start(self):
        threads = list()
        for threadid in range(self.number_thread):
            worker = multiprocessing.Process(
                target=self.down_task, args=(self.q,))
            worker.daemon = True
            worker.start()
            threads.append(worker)

        for song in self.songs:
            self.q.put(song)
        self.q.join()

        for p in threads:
            self.q.put(None)
        self.q.join()

        for thread in threads:
            thread.join()

        print 'Download Done!'
