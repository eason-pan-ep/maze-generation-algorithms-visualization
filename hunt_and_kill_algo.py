import random

class HuntAndKillAlgorithm():
    '''
    Class -- HuntAndKillAlgorithm 
    '''
    
    global MOVING_DIRECTIONS  # 4 possible moving direction, up, down, left, right
    MOVING_DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]  
    
    
    
    def __init__(self, grid_size:int, starting_position:tuple) -> None:
        '''
        Function -- __init__ initialize the algorithm class

        Parameters:
            grid_size -- how many cells on rows and columns,
                            e.g. 3 means 3x3, 4 means 4x4
        '''
        if(not isinstance(grid_size, int)):
            raise TypeError("Make sure grid_size is an integer")
        
        if(not isinstance(starting_position, tuple)):
            raise TypeError("Make sure starting_position is a tuple")
        
        if(not isinstance(starting_position[0], int) or (not isinstance(starting_position[1], int))):
            raise TypeError("Make sure the given position is a tuple of integers")
        
        if ((starting_position[0] < 0) or (starting_position[0] > (grid_size - 1)) 
            or (starting_position[1] < 0) or (starting_position[1] > (grid_size - 1))):
            raise ValueError("Given starting position out of grid")
        
        self.grid_size = grid_size  # Grid size
        self.grid = [[1 for i in range(self.grid_size)] for j in range(self.grid_size)]  # 2D list as the maze, 1 for unvisited, 0 for visited
        self.visited = [[False for i in range(self.grid_size)] for j in range(self.grid_size)]  # 2D list for logging visiting status of each cell
        
        # put starting position as (0, 0)
        self.current_pos = starting_position  # tracking current visiting cell
        self.visited_count = 1  ## trakcing how many cells have been visited
        self.grid[self.current_pos[0]][self.current_pos[1]] = 0
        self.visited[self.current_pos[0]][self.current_pos[1]] = True
        
        
    
    def hunt_and_kill(self) -> None:
        '''
        Function -- hunt_and_kill
            the primary algorithm implementation
        '''
       
        TOTAL_CELL_COUNT = self.grid_size * self.grid_size
        
        # !! Code for visualization in Terminal !!
        round_count = 1
        print("Round %d:" % round_count)
        # !! end !!
        
        while self.visited_count < TOTAL_CELL_COUNT: 
            # Hunting Phase, find unvisited neighbours
            unvisited_neiggbours = []
            
            # exploring 4 directions from the current position
            for move in MOVING_DIRECTIONS:
                neighbour_x = self.current_pos[0] + move[0]
                neighbour_y = self.current_pos[1] + move[1]
                
                if ((0 <= neighbour_x < self.grid_size) and (0 <= neighbour_y < self.grid_size) 
                    and (self.visited[neighbour_x][neighbour_y] == False)):
                    
                    unvisited_neiggbours.append((neighbour_x, neighbour_y))
                    
            # Killing Phase, carving passages from a random one of the unvisited neighbours
            if len(unvisited_neiggbours) > 0:
                (next_x, next_y) = random.choice(unvisited_neiggbours)
                self.grid[next_x][next_y] = 0
                self.visited[next_x][next_y] = True
                self.visited_count += 1
                self.current_pos = (next_x, next_y)
            else:
                self.find_next_start_position()
                
                # !! Below are code for visualization in terminal !!
                round_count += 1
                for row in self.grid:
                    print(row)
                print("--------------------------------------")
                print("Round %d:" % round_count)
                # !! end !!
            
            
                            
                
    
    def find_next_start_position(self) -> None:
        '''
        Function -- find_next_start_position 
            helper method for finding the next starting position
        '''
        for row_index in range(self.grid_size):
                    for col_index in range(self.grid_size):
                        if ((self.visited[row_index][col_index] == False) and 
                            (self.has_visited_neighbours(row_index, col_index))):
                            self.current_pos = (row_index, col_index)
                            self.grid[row_index][col_index] = 0
                            self.visited[row_index][col_index] = True
                            self.visited_count += 1
                            return
    
        
                
    def has_visited_neighbours(self, x:int, y:int) -> bool:
        '''
        Function -- has_visited_neighbours 
            Helper method to check whether there is at least one visited neighbour around the given position

        Parameters:
            x -- x coordinate of current position
            y -- y coordinate of current position

        Returns:
            True, if there is at least 1 visited neighbour
            otherwise, return False
        '''
        for move in MOVING_DIRECTIONS:
            neighbour_x = x + move[0]
            neighbour_y = y + move[1]
            if((0 <= neighbour_x < self.grid_size) and 
               (0 <= neighbour_y < self.grid_size) and 
               (self.visited[neighbour_x][neighbour_y] == True)):
                return True
        
        return False
    
    