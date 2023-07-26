import tkinter

class Cell:
    
    global LINE_COLOUR, CURRENT_FILL, ROAD_FILL
    
    LINE_COLOUR = "#FFFFFF"
    CURRENT_FILL = "#E4EFFF"
    ROAD_FILL = "#E4987F"
    
    def __init__(self, x, y, border_size) -> None:
        '''
        Method -- __init__ constructor

        Parameters:
            x -- col / x coordinate of this cell
            y -- row / y coordinate of this cell
            border_size -- wall thickness
        '''
        self.x = x
        self.y = y
        self.walls = {
            "top" : True,
            "bottom" : True,
            "left" : True,
            "right" : True,
        }
        self.is_visited = False
        self.border = border_size
        
        
        
    def draw_walls(self, canvas:tkinter.Canvas, tile_size:int) -> None:
        '''
        Method -- draw_walls 
            draw walls of this cell, depending on the wall status in it's self.walls

        Parameters:
            canvas -- the main maze canvas
            tile_size -- size of each tile on the canvas
        '''
        x, y = self.x * tile_size, self.y * tile_size
        if self.walls["top"]:
            canvas.create_line(x, y, x + tile_size, y, fill=LINE_COLOUR, width=self.border)
        else:
            canvas.create_line(x, y, x + tile_size, y, fill=ROAD_FILL, width=self.border)
       
        if self.walls["right"]:
            canvas.create_line(x + tile_size, y, x + tile_size, y + tile_size, fill=LINE_COLOUR, width=self.border)
        else:
            canvas.create_line(x + tile_size, y, x + tile_size, y + tile_size, fill=ROAD_FILL, width=self.border)

        if self.walls["bottom"]:
            canvas.create_line(x + tile_size, y + tile_size, x , y + tile_size, fill=LINE_COLOUR, width=self.border)
        else:
            canvas.create_line(x + tile_size, y + tile_size, x , y + tile_size, fill=ROAD_FILL, width=self.border)
      
        if self.walls["left"]:
            canvas.create_line(x, y + tile_size, x, y, fill=LINE_COLOUR, width=self.border)
        else:
            canvas.create_line(x, y + tile_size, x, y, fill=ROAD_FILL, width=self.border)


            
    def draw_current_status(self, canvas:tkinter.Canvas, tile_size:int) -> None:
        '''
        Method -- draw_current_status
            draw the colour as the head

        Parameters:
            canvas -- the main maze canvas
            tile_size -- size of each tile on the canvas
        '''
        x, y = self.x * tile_size, self.y * tile_size
        canvas.create_rectangle(x, y, x + tile_size, y + tile_size, fill=CURRENT_FILL)
        
    
    
    def draw_path(self, canvas:tkinter.Canvas, tile_size:int) -> None:
        '''
        Method -- draw_path 

        Parameters:
            canvas -- the main maze canvas
            tile_size -- size of each tile on the canvas
        '''
        x, y = self.x * tile_size, self.y * tile_size
        canvas.create_rectangle(x, y, x + tile_size, y + tile_size, fill=ROAD_FILL)
        
        
