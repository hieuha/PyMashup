#!/usr/bin/env python
# coding:utf-8

import zingmp3
import download
import lyric
import os

pattern = raw_input("Your words for matshup? ")

if pattern:
    print "Tenten, %s." % pattern
    zing = zingmp3.ZingMp3()
    yes = raw_input("Do you want to download? (yes/no)")
    if yes and yes == 'yes':
        print 'Download Top Zing Mp3 Music'
        songs = zing.top_song()
        infos = zing.songs_info(songs)
        my_download = download.Download(infos)
        my_download.start()
    my_lyric = lyric.Lyric()
    my_lyric.search(pattern)
    os.system("./split_and_merge_mp3.sh")

else:
    print 'exit'
