from __future__ import unicode_literals
import lyricsgenius

class Lyrics():
    song_name = ''
    song_artist = ''
    def __init__(self, song, artist):
        self.song_name = song
        self.song_artist = artist
 
    def lyrics(self):
        genius = lyricsgenius.Genius("XiGHD1n8XJcyXaxfrFdmx1C7MgV3ZMLcPbq_5U9Mi_xmWjVyPbs9GXlfRmjJb4_o")
      
        song = genius.search_song(self.song_name, self.song_artist)
        print(song.lyrics)

def get_lyrics():
    songname = input("Song Name: ")
    artistname = input("Artist Name: ")
    lyrics_obj = Lyrics(songname, artistname)
    lyrics_obj.lyrics() 