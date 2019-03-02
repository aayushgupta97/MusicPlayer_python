from __future__ import unicode_literals
import os
import pygame
import math 
import youtube_dl
from random import randint,shuffle
# import random
# import sys
pygame.init()

default = os.listdir('music/')
# print(default)
favourite = [] 
current = [] 

#Makes a list of favourite songs from the text file
with open('fav.txt', 'r') as f:
    favourite = [line.strip() for line in f]
# f.close() 

def favourites(item):
    # os.chdir('../')
    with open('../fav.txt', 'a') as f : 
        f.write(item)
        f.write("\n")
    # f.close()
    favourite.append(item)
    # os.chdir('music/') 


# print("this is favourite playlist \n")
# print(favourite)

os.chdir("music/")

all_playlist = [default, current, favourite]

# Plays all songs in the selected playlist
def play_playlist(lst):
    print("Playing all the songs in the selected playlist\n")
    print("next - to play the next song in playlist\n")
    print("stop - to stop the playback and return to main menu\n")
    print("fav - to add to favourites\n")
    print("pause - to pause the playback\n")
    print("play - to resume the playback\n")
    
    

    play = True
    while play:
        for song in lst:
            pygame.mixer.music.load(song)
            print("\n" + "-"*150 + "\n" + "Currently Playing : " + song)
            a = pygame.mixer.Sound(song)
            print("length: ",int(a.get_length()//60),"min",math.floor(a.get_length())%60,"seconds")
            print('-' * 150)
            pygame.mixer.music.play(0)
            
            playing = True
            while playing:
                c = input("what do you want to do:")
                if c=='next': # exits this while loop
                    pygame.mixer.music.stop()
                    playing = False
                elif c=='stop': # exits all the loops
                    pygame.mixer.music.stop()
                    playing = False
                    # break
                elif c=='fav':
                    favourites(song)
                elif c=='pause':
                    pygame.mixer.music.pause()
                elif c=='play':
                    pygame.mixer.music.unpause()
                elif c=='main':
                    main()
            
                else:
                    print("Invalid Input! Try (play,pause,stop,fav,next) ")
            if c=='stop':
                play = False
                break

    main()


    # main()

# Select the playlist to use
def select_playlist():
    default = os.listdir()

    print("Enter the playlist you want to play: \n")
    print("0 : default playlist (all songs)\n")
    print("1 : current playlist \n")
    print("2 : Favourite playlist\n")
    lst_id = int(input("Enter the ID of the playlist to play: "))
    
    if lst_id > 2 or lst_id < 0:
        print("You have entered an invalid index. returning to main menu.")
        main() 
   

    show_playlist(all_playlist[lst_id])
    print("\n1) Play the list\n2) Edit the list\n3) Shuffle the list")
    # choice = int(input("Enter your choice: "))
    choice = input("Enter your choice: ")

    if choice == '1' :     
        print(f"Playing the playlist {all_playlist[lst_id]} ")
        play_playlist(all_playlist[lst_id])
    elif choice == '2' : 
        addto_playlist(all_playlist[lst_id])
    elif choice == '3' : 
        shuffle_playlist(all_playlist[lst_id])
    else: 
        print("\nInvalid Input. Returning to main menu. ")
        main() 

#Shows all the songs in the passed playlist
def show_playlist(lst):
    length = len(lst)
    indexes = [i for i in range(length)]
    c = list(zip(indexes,lst))
    print("*" * 150)
    for i in c:
        print(i[0],"---->", i[1])
    print("*" * 150)
    
    # main() 
# playlist(default)

# Add or remove the song from the selected playlist
def addto_playlist(lst):
    # print("Press 1 to add songs to the current playlist")
    # print("Press 2 to remove songs from the current playlist")
    flag = 'y'
    show_playlist(default)

    while flag=='y': 
        try: 
            choice = input("Press a to Add and r to Remove from playlist: ")
        # show_playlist(default)
            c = int(input("Enter the index of the song to be added/removed: "))
            if choice == 'a':
                lst.append(default[c])
                show_playlist(lst)
            elif choice == 'r':
                lst.pop(c)
                show_playlist(lst)
             
            else: 
                print("Invalid Choice.")
        except: 
                IndexError
                print("Invalid index try again.")
        finally: 
            flag = input("Would you like to add/remove another song? (y/n)")
        
    # Rewrite the fav file if favourite playlist is changed.
    if lst==favourite:
        with open('../fav.txt', 'w') as f:
            for item in lst:
                f.write("%s\n" % item)
                # f.write(item)
                # f.write("\n")
        # f.close()
    
    print("Edited the list. Now playing the playlist. \n")
    show_playlist(lst)
    play_playlist(lst)
# playlist()
# play_all() 
# plays all the songs in default playlist or directory 

# select_playlist()




#to play a specific song
def play_song(id):
    pygame.mixer.music.load(default[id])
    print(default[id])
    pygame.mixer.music.play(0)
    c = input("press y to go back to main menu.")
    if c=='y':
        pygame.mixer.music.stop()
        print("okay stopping all songs.")
        main()
    else:
        end()
def songs():
    show_playlist(default)
    song_id = int(input("What song would you like to play? "))
    play_song(song_id)


def greeting():
    print("Welcome to CLI Music Player\n")
    print("\nUse on screen instructions to navigate\n")
    main()
def end():
    print("goodbye!")   
    exit()
def main():
    print("\n\n\n")
    print("-"*150 + "\n" + "*" * 150)
    print("Press 1 to select playlist")
    # print("Press 2 to list all songs")
    print("press 2 to select a song")
    print("press 3 to shuffle all songs")
    print("press 5 to for lyrics")
    

    print("press 7 to sort all songs by time or name")
    print("press 8 to download a song from youtube")
    print("press 9 to exit")
    print("*"*150 + "\n" + "-" * 150)

    my_dict = {
        1:select_playlist,
        # 2:playlist,
        2:songs,
        3:shuffle_playlist,
        5:lyrics,
        6:main_test,
        7:sort_playlist,
        8:youtube,
        9:end
    }
    c = int(input("\nWhat would you like to do?"))
    my_dict.get(c,lambda:'Invalid')()

def youtube():
    # from __future__ import unicode_literals

    # import youtube_dl
    link = []
    linkinput = input("Enter the url you want to download: ")
    link.append(linkinput)
    ydl_opts = {
            'format': 'best',
            # 'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'vorbis',
            'preferredquality': '320',
            #  'nopostoverwrites': True
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(['https://www.youtube.com/watch?v=ZkqyIoYAXV8'])
        ydl.download(link)
        # default = os.listdir()
        # print(default)
    main()
# shuffled_playlist = [] 

def shuffle_playlist(lst=default):
    # shuffling = 'y'
    # while shuffling=='y' :
    #     p = randint(0,len(lst)-1)
    #     pygame.mixer.music.load(lst[p])
    #     pygame.mixer.music.play(0)
    #     # main()
    #     shuffling = input("listen to next song? y/n: ")
    shuffled_playlist = lst[:]
    shuffle(shuffled_playlist)
    # print(shuffled_playlist)

    play_playlist(shuffled_playlist)

import glob
# import os

 
def sort_playlist(lst=default):
    # mtime = lambda f: os.stat(os.path.join(lst, f)).st_mtime
    # sorted_list =  list(sorted(os.listdir(lst), key=mtime))
    # print(sorted_list)
    c = input("\n N to sort by name \n D to sort by Date: ")
    
    if c=='d':
        files = glob.glob("*.ogg")
        files.sort(key=os.path.getmtime)
        print("\n".join(files))         
    elif c=='n':
        for x in sorted(lst):
            print(x)
    else: 
        print("Invalid selection")
    main()     
import lyricsgenius

def lyrics():
    genius = lyricsgenius.Genius("XiGHD1n8XJcyXaxfrFdmx1C7MgV3ZMLcPbq_5U9Mi_xmWjVyPbs9GXlfRmjJb4_o")
    # artist = genius.search_artist("Arijit", max_songs=3)
    # print(artist.songs)
    # song = genius.search_song("turn the page", 'metallica')
    songname = input("enter the name of the song")
    artistname = input("enter the name of the artist")
    song = genius.search_song(songname, artistname)
    print(song.lyrics)

def main_test():
    pass   
greeting()
# select_playlist()



