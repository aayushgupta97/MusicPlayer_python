from __future__ import unicode_literals
import youtube_dl

class Youtube():
    url = []
    def __init__(self, input_url):
        self.url.append(input_url)

    def youtube(self):
        ydl_opts = {
            'format': 'best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'vorbis',
                'preferredquality': '320',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.url)
# lyrics.tc_lyrics()   

def download_from_youtube():
    linkinput = input("Enter the url you want to download: ")
    youtube_object = Youtube(linkinput)
    youtube_object.youtube()
