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
        self.border = 3
        
    def draw_walls(self, screen, tile_size) -> None:
        FILL_COLOUR = "#525252"
        LINE_COLOUR = "#FF9330"
        
        x, y = self.x * tile_size, self.y * tile_size

        if self.walls["top"]:
            pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (x, y), (x + tile_size, y), self.border)
        if self.walls["right"]:
            pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (x + tile_size, y), (x + tile_size, y + tile_size), self.border)
        if self.walls["bottom"]:
            pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (x + tile_size, y + tile_size), (x , y + tile_size), self.border)
        if self.walls["left"]:
            pygame.draw.line(screen, pygame.Color(LINE_COLOUR), (x, y + tile_size), (x, y), self.border)
            
            