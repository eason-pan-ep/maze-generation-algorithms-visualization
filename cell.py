import pygame

class Cell:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.walls = {
            "top" : True,
            "bottom" : True,
            "left" : True,
            "right" : True,
        }
        self.is_visited = False
        self.size = 5
        
    def draw_walls(self, screen:int, tile_size:int) -> None:
        FILL_COLOUR = "#FFFFFF"
        LINE_COLOUR = "#FFAC30"
        BORDER_WIDTH = 2
        
        draw_x = self.x * tile_size
        draw_y = self.y * tile_size
        
        # if this cell is visited, fill it with white
        if (self.is_visited):
            #fill colour
            pygame.draw.rect(screen, pygame.Color(FILL_COLOUR), (draw_x, draw_y, tile_size, tile_size))
            if(self.walls["top"]):
                pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (draw_x, draw_y), (draw_x + tile_size, draw_y + tile_size), BORDER_WIDTH)
            if(self.walls["bottom"]):
                pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (draw_x, draw_y + tile_size), (draw_x + tile_size, draw_y + tile_size), BORDER_WIDTH)
            if(self.walls["left"]):
                pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (draw_x, draw_y), (draw_x, draw_y + tile_size), BORDER_WIDTH)
            if(self.walls["right"]):
                pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (draw_x + tile_size, draw_y), (draw_x + tile_size, draw_y + tile_size), BORDER_WIDTH)
            
            