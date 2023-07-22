import random

class HuntAndKillAlgorithm():
    '''
    Class -- HuntAndKillAlgorithm 
    '''
    
    def __init__(self, grid_size) -> None:
        '''
        Function -- __init__ initialize the algorithm class

        Parameters:
            grid_size -- how many cells on rows and columns,
                            e.g. 3 means 3x3, 4 means 4x4
        '''
        self.grid_size = grid_size  # Grid size
        self.grid = [[1 for i in range(self.grid_size)] for j in range(self.grid_size)]  # 2D list as the maze
        self.visited = [[False for i in range(self.grid_size)] for j in range(self.grid_size)]  # 2D list for logging visiting status of each cell
        self.current_pos = (0, 0)  # tracking current visiting cell
        self.visited_count = 0  ## trakcing how many cells have been visited
        
    
    
    