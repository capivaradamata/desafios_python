import pygame
pygame.init()
pygame.mixer.music.load('desafioaudio.mp3')
input(pygame.mixer.music.play())
pygame.event.wait()