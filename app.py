import os
import pygame
pygame.init()

default = os.listdir('music/')
print(default)
os.chdir("music/")
favourite = [] 
current = [] 
all_playlist = [default, current, favourite]

# Plays all songs in the selected playlist
def play_playlist(lst):
    print("Playing all the songs in the selected playlist\n")
    print("next - to play the next song in playlist\n")
    print("stop - to stop the playback\n")
    play = True
    while play:
        for song in lst:
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
    # main()

# select the playlist to use
def select_playlist():
    print("Enter the playlist you want to play: \n")
    print("0 : default playlist (all songs)\n")
    print("1 : current playlist \n")
    print("2 : Favourite playlist\n")
    lst_id = int(input("Enter the ID of the playlist to play: "))
    show_playlist(all_playlist[lst_id])
    print("\n1) Play the list\n2)Edit the list\n")
    choice = int(input("Enter your choice: "))
    if choice == 1 :     
        print(f"Playing the playlist {all_playlist[lst_id]} ")
        play_playlist(all_playlist[lst_id])
    elif choice == 2 : 
        addto_playlist(all_playlist[lst_id])

#Shows all the songs in the passed playlist
def show_playlist(lst):
    length = len(lst)
    indexes = [i for i in range(length)]
    c = list(zip(indexes,lst))
    for i in c:
        print(i)
    # main() 
# playlist(default)

# Add or remove the songs from playlist
def addto_playlist(lst):
    # print("Press 1 to add songs to the current playlist")
    # print("Press 2 to remove songs from the current playlist")
    flag = 'y'
    show_playlist(default)

    while flag=='y': 
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
        flag = input("Would you like to add/remove another song? (y/n)")
    print(lst)
    print("Edited the list. Now playing the playlist. \n")
    play_playlist(lst)
# playlist()
# play_all() 
# plays all the songs in default playlist or directory 

select_playlist()






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

# greeting()
# select_playlist()

