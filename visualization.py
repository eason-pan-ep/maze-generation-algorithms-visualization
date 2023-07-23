import pygame
from random import choice

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
TILE = 50

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
    screen.fill(pygame.Color("darkgray"))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    
    pygame.display.flip()
    
    
