import playlist 
import youtube
import lyrics
import song
def main_menu():
    """has the options the the users selects to navigate.
    Has a True loop so after every executed function the user returns here.
    """
    musicplayer = True
    while musicplayer:
        print("\n\n\n")
        print("-"*150 + "\n" + "*" * 150)
        print("Press 1 to select playlist\
                \npress 2 to select a song\
                \npress 3 to play recently added songs\
                \npress 4 to search for lyrics\
                \npress 5 to download a song from youtube\
                \npress 9 to exit")
        print("*"*150 + "\n" + "-" * 150)

        my_dict = {
            1: playlist.select_playlist,
            2: song.select_song,
            3: playlist.sort_playlist,
            4: lyrics.get_lyrics,
            5: youtube.download_from_youtube,
            9: end
        }
        user_choice = int(input("\nWhat would you like to do?"))
        my_dict.get(user_choice, lambda: 'Invalid')()


def greeting():
    """called when the program starts and calls the main menu"""
    print("\nCLI Music Player\n\
        \nUse on screen instructions to navigate\n")
    main_menu()


def end():
    """exits the program immediately using the sys.exit() whenever called"""
    print("goodbye!")
    exit()

greeting()