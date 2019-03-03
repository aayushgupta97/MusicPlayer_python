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

    # def __init__(self, selected_playlist):
    def play_playlist(self, selected_playlist):
        print("Playing all the songs in the selected playlist\n")
        print("next - to play the next song in playlist\n")
        print("stop - to stop the playback and return to main menu\n")
        print("fav - to add to favourites\n")
        print("pause - to pause the playback\n")
        print("play - to resume the playback\n")
        print("main - to resume the playback\n")
        print("lyrics - to resume the playback\n")
        

        play = True
        while play:
            for song in selected_playlist:
                pygame.mixer.music.load(song)
                print("\n" + "-"*150 + "\n" + "Currently Playing : " + song)
                a = pygame.mixer.Sound(song)
                print("length: ", int(a.get_length()//60), "min",
                    math.floor(a.get_length()) % 60, "seconds")
                print('-' * 150)
                pygame.mixer.music.play(0)

                playing = True
                while playing:
                    c = input("what do you want to do:")
                    if c == 'next':  # exits this while loop
                        pygame.mixer.music.stop()
                        playing = False
                    elif c == 'stop':  # exits all the loops
                        pygame.mixer.music.stop()
                        playing = False
                        # break
                    elif c == 'fav':
                        self.favourites(song)
                    elif c == 'pause':
                        pygame.mixer.music.pause()
                    elif c == 'play':
                        pygame.mixer.music.unpause()
                    elif c == 'main':
                        playing = False
                    elif c == 'lyrics':
                        lyrics.get_lyrics()

                    else:
                        print("Invalid Input! Try (play,pause,stop,fav,next) ")
                if c == 'stop' or c == 'main':
                    play = False
                    break

        # main()
   
    def show_playlist(self, selected_playlist):
        length = len(selected_playlist)
        indexes = [i+1 for i in range(length)]
        c = list(zip(indexes, selected_playlist))
        print("*" * 150)
        for i in c:
            print(i[0], "---->", i[1])
        print("*" * 150)

    def addto_playlist(self, selected_playlist):
        flag = 'y'
        self.show_playlist(default)

        while flag == 'y':
            try:
                choice = input("Press a to Add and r to Remove from playlist: ")
                c = int(input("Enter the index of the song to be added/removed: "))
                if choice == 'a':
                    selected_playlist.append(default[c])
                    self.show_playlist(selected_playlist)
                elif choice == 'r':
                    selected_playlist.pop(c)
                    self.show_playlist(selected_playlist)

                else:
                    print("Invalid Choice.")
            except:
                IndexError
                print("Invalid index try again.")
            finally:
                flag = input("Would you like to add/remove another song? (y/n)")

        # Rewrite the fav file if favourite playlist is changed.
        if selected_playlist == favourite:
            with open('../fav.txt', 'w') as f:
                for item in selected_playlist:
                    f.write("%s\n" % item)

        print("Edited the list. Now playing the playlist. \n")
        self.show_playlist(selected_playlist)
        self.play_playlist(selected_playlist)

    def shuffle_playlist(self, selected_playlist=default):
        shuffled_playlist = selected_playlist[:]
        shuffle(shuffled_playlist)
        self.show_playlist(shuffled_playlist)
        self.play_playlist(shuffled_playlist)


    def sort_playlist(self, selected_playlist = default):
        c = input("\n N to sort by name \n D to sort by Date: ")

        if c == 'd':
            files = glob.glob("*.ogg")
            files.sort(key=os.path.getmtime)
            print("\n".join(files))
        elif c == 'n':
            for x in sorted(selected_playlist):
                print(x)
        else:
            print("Invalid selection")
        # main()


    def favourites(self, item):
            with open('../fav.txt', 'a') as f:
                f.write(item)
                f.write("\n")
            favourite.append(item)

def select_playlist():
    playlist_object = Playlist()
    default = os.listdir()

    print("Enter the playlist you want to play: \n")
    print("0 : default playlist (all songs)\n")
    print("1 : current playlist \n")
    print("2 : Favourite playlist\n")
    lst_id = int(input("Enter the ID of the playlist to play: "))

    if lst_id > 2 or lst_id < 0:
        print("You have entered an invalid index. returning to main menu.")
        # main()

    playlist_object.show_playlist(all_playlist[lst_id])
    print("\n1) Play the list\n2) Edit the list\n3) Shuffle the list")
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Playing the playlist {all_playlist[lst_id]} ")
        playlist_object.play_playlist(all_playlist[lst_id])
    elif choice == '2':
        playlist_object.addto_playlist(all_playlist[lst_id])
    elif choice == '3':
        playlist_object.shuffle_playlist(all_playlist[lst_id])
    else:
        print("\nInvalid Input. Returning to main menu. ")
        # main()

def shuffle_playlist(lst=default):
    shuffleobj = Playlist()
    shuffled_playlist = lst[:]
    shuffle(shuffled_playlist)
    shuffleobj.show_playlist(shuffled_playlist)
    shuffleobj.play_playlist(shuffled_playlist)

def sort_playlist(lst=default):
    sortobj = Playlist()
    # path = '/path/to/files/'
    # name_list = os.listdir(path)
    name_list = default[:]
    path = ''
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getctime)
    time_sorted_list.reverse()
    sortobj.show_playlist(time_sorted_list)
    sortobj.play_playlist(time_sorted_list)
