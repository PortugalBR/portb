import pygame as pygame
pygame.init()
mixer.music.music.load('ex14.mp3')
mixer.music.play()
input('Agora você escuta?')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()