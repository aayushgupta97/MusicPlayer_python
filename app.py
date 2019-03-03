import playlist
import youtube
import lyrics
musicplayer = True
def main_menu():

    while musicplayer:
        print("\n\n\n")
        print("-"*150 + "\n" + "*" * 150)
        print("Press 1 to select playlist")
        print("press 2 to select a song")
        print("press 3 to shuffle all songs")
        print("press 5 to for lyrics")
        print("press 7 to play recently added songs")
        print("press 8 to download a song from youtube")
        print("press 9 to exit")
        print("*"*150 + "\n" + "-" * 150)

        my_dict = {
            1: playlist.select_playlist,
            # 2: song.play_song,
            3: playlist.shuffle_playlist,
            5: lyrics.get_lyrics,
            # 6: main_test,
            7: playlist.sort_playlist,
            8: youtube.download_from_youtube,
            9: end
        }
        user_choice = int(input("\nWhat would you like to do?"))
        my_dict.get(user_choice, lambda: 'Invalid')()


def greeting():
    print("Welcome to CLI Music Player\n")
    print("\nUse on screen instructions to navigate\n")
    main_menu()


def end():
    print("goodbye!")
    exit()


# youtube.download_from_youtube()
# lyrics.get_lyrics()
greeting()
