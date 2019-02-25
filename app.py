# import pygame
# from pygame import mixer
# mixer.init() 
# vol = mixer.music.get_volume()

# print(vol)
# mixer.music.load('Turn the Page.ogg')
# mixer.music.play()
# mixer.music.stop()
# import vlc
# p = vlc.MediaPlayer("Turn the Page.ogg")
# p.play()


# class player: 
#     def __init__(): 
#         pass
import os
import pygame
pygame.init()
# pygame.display.set_mode((200,100))

# pygame.mixer.music.load("Turn the Page.ogg")
# pygame.mixer.music.play(0)
# # input("what do you want to do:")
# if input=='stop':
#     pygame.mixer.music.stop()

songs = os.listdir('music/')
print(songs)
os.chdir("music/")

for song in songs:
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)
    input("what do you want to do:")
    if input=='stop':
        pygame.mixer.music.stop()
    

def check():
    
# input("what do you want to do:")
# if input=='stop':
#     pygame.mixer.music.stop()

# clock = pygame.time.Clock()
# clock.tick(10)
# while pygame.mixer.music.get_busy():
#     pygame.event.poll()
#     clock.tick(10)


    