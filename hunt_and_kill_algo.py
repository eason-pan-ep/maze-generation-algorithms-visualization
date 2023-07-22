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
        self.grid = []  # 2D list as the maze
        self.visited = []  # 2D list for logging visiting status of each cell
        self.current_pos = (0, 0)  # tracking current visiting cell
        self.visited_count = 0  ## trakcing how many cells have been visited
        
    
    def initialize_algorithm(self):
        '''
        Function -- initialize_algorithm 
            initialize the grid and visited log
        '''
        self.initialize_grid()
        
    
    def initialize_grid(self):
        '''
        Function -- initialize_grid 
            initialize grid and fill all of them with 1
        '''
        for row in range(self.grid_size):
            pass
            
    
    def initialize_visited(self):
        '''
        Function -- initialize_visited 
            initialize visited log
        '''
        pass
    