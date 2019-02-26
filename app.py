import os
import pygame
pygame.init()

default = os.listdir('music/')
print(default)
os.chdir("music/")


def play_all():
    print("Playing all the songs\n")
    print("next - to play the next song in playlist\n")
    print("stop - to stop the playback\n")
    play = True
    while play:
        for song in default:
                pygame.mixer.music.load(song)
                print(song)
                pygame.mixer.music.play(0)
                c = input("what do you want to do:")
                if c=='next':
                    pygame.mixer.music.stop()
                if c=='stop':
                    pygame.mixer.music.stop()
                    play = False
                    break
    main()

def show_playlist(lst):
    length = len(lst)
    indexes = [i for i in range(length)]
    c = list(zip(lst,indexes))
    for i in c:
        print(i)
    main() 
# playlist(default)

#Shows all the songs in the passed playlist
def playlist():
    show_playlist(default)
# play_all() 
# plays all the songs in default playlist or directory 




#to play a specific song
def play_song(id):
    pygame.mixer.music.load(default[id])
    print(default[id])
    pygame.mixer.music.play(0)
    c = input("what next?")
    if c=='stop':
        pygame.mixer.music.stop()
        print("okay stopping all songs.")
        main()
def songs():
    song_id = int(input("What song would you like to play? "))
    play_song(song_id)


def greeting():
    print("Welcome to CLI Music Player\n")
    print("\nUse on screen instructions to navigate\n")
    main()
def end():
    print("goodbye!")   
def main():
    print("Press 1 to play all songs")
    print("Press 2 to list all songs")
    print("press 3 to select a song")
    print("press 9 to exit")
    my_dict = {
        1:play_all,
        2:playlist,
        3:songs,
        9:end
    }
    c = int(input("\nWhat would you like to do?"))
    my_dict.get(c,lambda:'Invalid')()

greeting()
