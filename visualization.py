import pygame
from cell import *
from random import choice

def main():
    TILE_SIZE = 50
    COLUMN_COUNT = 10
    ROW_COUNT = 10

    # !! standard pygame framework start here !!
    pygame.init()
    screen_width = COLUMN_COUNT * TILE_SIZE
    scrren_height = ROW_COUNT * TILE_SIZE
    screen = pygame.display.set_mode((screen_width, scrren_height))
    clock = pygame.time.Clock()
    
    grid = [[Cell(col, row) for row in range(ROW_COUNT)] for col in range(COLUMN_COUNT)]
    current_position = grid[0][0]
    
    

    # pygame running mainloop
    while True:
        screen.fill(pygame.Color("#525252"))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
        
        pygame.display.flip()
        clock.tick(30)
    # !! standard pygame framework ends !!
    
    
if __name__ == "__main__":
    main()