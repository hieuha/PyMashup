
import zingmp3
import download

zing = zingmp3.ZingMp3()

songs = zing.top_song(3)
infos = zing.songs_info(songs)
my_download = download.Download(infos)
my_download.start()
