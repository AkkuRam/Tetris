import pygame
import sys

width = 800
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.init()

game_over = False

while not game_over: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()