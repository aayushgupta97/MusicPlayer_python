from playlist import Playlist
import pygame
import os

default = os.listdir('/home/ttn/Documents/MusicProject/src/music/')
default = sorted(default)
class Song:
    def __init__(self, song_id):
        self.song_id = song_id
    def play_song(self):
        """
        takes the input from the select_song function and plays the song 
        at the selected id
        """
        pygame.mixer.music.load(default[self.song_id])
        print(default[self.song_id])
        pygame.mixer.music.play(0)
        choice = input("press y to go back to main menu.")
        if choice == 'y':
            pygame.mixer.music.stop()
            print("stopping playback.")
        else:
            exit()

def select_song():
    """Take an integer input for the id and plays the song at the 
    selected id in the default playlist.
    """
    play_list = Playlist(default)
    play_list.show_playlist()
    song_id = int(input("What song would you like to play? "))
    song_id -= 1
    song_object = Song(song_id)
    song_object.play_song()



