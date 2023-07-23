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
        
    def draw_walls(self, )