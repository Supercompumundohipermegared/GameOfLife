import pygame
import sys

pygame.display.init()

x = int(input("X? "))
y = int(input("Y? "))

pantalla = pygame.display.set_mode(size=(x, y), depth=0, display=0, vsync=0)
pygame.display.init()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
