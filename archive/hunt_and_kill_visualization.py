import pygame
from random import choice
from cell import *

TILE_SIZE = 50
COLUMN_COUNT = 10
ROW_COUNT = 10



def main():
    
    # !! standard pygame framework !!
    pygame.init()
    screen_width = COLUMN_COUNT * TILE_SIZE + 4
    scrren_height = ROW_COUNT * TILE_SIZE + 4

    screen = pygame.display.set_mode((screen_width, scrren_height))
    clock = pygame.time.Clock()
    
    # initialize the grid
    grid = [[Cell(col, row) for row in range(ROW_COUNT)] for col in range(COLUMN_COUNT)]
    current_position = grid[0][0]
    

    # pygame running mainloop
    while True:
        screen.fill(pygame.Color("#525252"))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        #initialize all cells
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                grid[row][col].draw_walls(screen, TILE_SIZE)
        
        pygame.display.flip()
        clock.tick(30)
    # !! standard pygame framework ends !!
    


if __name__ == "__main__":
    main()