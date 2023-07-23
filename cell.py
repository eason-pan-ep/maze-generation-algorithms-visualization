import tkinter

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
        
    def draw_walls(self, canvas:tkinter.Canvas, tile_size:int) -> None:
        FILL_COLOUR = "#525252"
        LINE_COLOUR = "#FF9330"
        
        x, y = self.x * tile_size, self.y * tile_size

        if self.walls["top"]:
            canvas.create_line(x, y, x + tile_size, y, fill=LINE_COLOUR, width=self.border)
       
        if self.walls["right"]:
            canvas.create_line(x + tile_size, y, x + tile_size, y + tile_size, fill=LINE_COLOUR, width=self.border)

        if self.walls["bottom"]:
            canvas.create_line(x + tile_size, y + tile_size, x , y + tile_size, fill=LINE_COLOUR, width=self.border)
      
        if self.walls["left"]:
            canvas.create_line(x, y + tile_size, x, y, fill=LINE_COLOUR, width=self.border)

            
            