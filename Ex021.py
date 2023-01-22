# reproduzir arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('Ex021-file.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
