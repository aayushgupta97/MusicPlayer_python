import pygame
import math
from random import shuffle
import os 
import lyrics
pygame.init()

default = os.listdir('music/')
default = sorted(default)
favourite = []
current = []

# Makes a list of favourite songs from the text file
with open('fav.txt', 'r') as f:
    favourite = [line.strip() for line in f]

os.chdir("music/")

all_playlist = [default, current, favourite]

class Playlist:

    def __init__(self, selected_playlist):
        self.selected_playlist = selected_playlist

    def play_playlist(self):
        """plays the selected playlist in an ordered or shuffled way"""
        print("Playing all the songs in the selected playlist\
            \n\nnext - to play the next song in playlist\
            \n\nstop - to stop the playback and return to main menu\
            \n\nfav - to add to favourites\
            \n\npause - to pause the playback\
            \n\nplay - to resume the playback\
            \n\nmain - to go back to the main menu\
            \n\nlyrics - to search for lyrics")
     
        play = True
        while play:
            for song in self.selected_playlist:
                pygame.mixer.music.load(song)
                print("\n" + "-"*150 + "\n" + "Currently Playing : " + song)
                current_song = pygame.mixer.Sound(song)
                print("length: ", int(current_song.get_length()//60), "min",
                    math.floor(current_song.get_length()) % 60, "seconds")
                print('-' * 150)
                pygame.mixer.music.play(0)

                playing = True
                while playing:
                    user_choice = input("what do you want to do:")
                    if user_choice == 'next':  
                        # exits this while loop
                        pygame.mixer.music.stop()
                        playing = False
                    elif user_choice == 'stop': 
                        # exits all the loops
                        pygame.mixer.music.stop()
                        playing = False
                        
                    elif user_choice == 'fav':
                        self.favourites(song)
                    elif user_choice == 'pause':
                        pygame.mixer.music.pause()
                    elif user_choice == 'play':
                        pygame.mixer.music.unpause()
                    elif user_choice == 'main':
                        playing = False
                    elif user_choice == 'lyrics':
                        lyrics.get_lyrics()

                    else:
                        print("Invalid Input! Try (play,pause,stop,fav,next) ")
                if user_choice == 'stop' or user_choice == 'main':
                    play = False
                    break

        
   
    def show_playlist(self):
        """shows the selected playlist item by item"""
        length = len(self.selected_playlist)
        indexes = [index+1 for index in range(length)]
        items = list(zip(indexes, self.selected_playlist))
        print("*" * 150)
        for item in items:
            print(item[0], "---->", item[1])
        print("*" * 150)

    def addto_playlist(self):
        """adds or removes songs from the selected playlist"""
        flag = 'y'
        for index in range(len(default)):
            print(index+1, default[index])


        while flag == 'y':
            try:
                choice = input("Press a to Add and r to Remove from playlist: ")
                song_id = int(input("Enter the index of the song to be added/removed: "))
                song_id-=1
                if choice == 'a':
                    if default[song_id] in self.selected_playlist:
                        print("Already added in the playlist.")
                    else:
                        self.selected_playlist.append(default[song_id])
                        self.show_playlist()
                elif choice == 'r':
                    self.selected_playlist.pop(song_id)
                    self.show_playlist()

                else:
                    print("Invalid Choice.")
            except:
                IndexError
                print("Invalid index try again.")
            finally:
                flag = input("Would you like to add/remove another song? (y/n)")

        # Rewrite the fav file if favourite playlist is changed.
        if self.selected_playlist == favourite:
            with open('../fav.txt', 'w') as f:
                for item in self.selected_playlist:
                    f.write("%s\n" % item)

        print("Edited the list. Now playing the playlist. \n")
        self.show_playlist()
        self.play_playlist()

    def shuffle_playlist(self):
        """shuffles the selected playlist inplace using random shuffle"""
        shuffle(self.selected_playlist)
        self.show_playlist()
        self.play_playlist()


    def favourites(self, item):
        """
        takes the currently playing song and adds it to favourite file and list
        params: item
        returns: 
        """
        with open('../fav.txt', 'a') as f:
            f.write(item)
            f.write("\n")
        favourite.append(item)

    

def select_playlist():
    """selects a playlist to play, shuffle or add or remove items"""
    default = os.listdir()

    print("Enter the playlist you want to play: \n")
    print("0 : default playlist (all songs)\n")
    print("1 : current playlist \n")
    print("2 : Favourite playlist\n")
    lst_id = int(input("Enter the ID of the playlist to play: "))

    if lst_id > 2 or lst_id < 0:
        print("You have entered an invalid index. returning to main menu.")
    
    playlist_object = Playlist(all_playlist[lst_id])
    playlist_object.show_playlist()

    print("\n1) Play the list\n2) Edit the list\n3) Shuffle the list")
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Playing the playlist {all_playlist[lst_id]} ")
        playlist_object.play_playlist()

    elif choice == '2':
        playlist_object.addto_playlist()

    elif choice == '3':
        playlist_object.shuffle_playlist()

    else:
        print("\nInvalid Input. Returning to main menu. ")
        

def sort_playlist(lst=default):
    """sorts the selected playlist according to the time of modification.
    Recently added songs in the directory come on top.
    """
    name_list = default[:]
    path = ''
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getctime)
    time_sorted_list.reverse()
    sortobj = Playlist(time_sorted_list)
    sortobj.show_playlist()
    sortobj.play_playlist()

