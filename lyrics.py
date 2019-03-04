from __future__ import unicode_literals
import lyricsgenius

class Lyrics():
    song_name = ''
    song_artist = ''
    def __init__(self, song, artist):
        self.song_name = song
        self.song_artist = artist
 
    def lyrics(self):
        genius = lyricsgenius.Genius("client-access-token here")
      
        song = genius.search_song(self.song_name, self.song_artist)
        print(song.lyrics)

def get_lyrics():
    """takes song and artist and input and searches for lyrics"""
    songname = input("Song Name: ")
    artistname = input("Artist Name: ")
    lyrics_obj = Lyrics(songname, artistname)
    lyrics_obj.lyrics() 
