from random import choice
import cell

global MOVING_DIRECTIONS  # 4 possible moving direction, up, down, left, right
MOVING_DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def hunt_and_kill(main_grid:list, visited_status:list, current_cell:cell.Cell, grid_width:int) -> cell.Cell or None:
    '''
    Function -- hunt_and_kill 
        running hunt-and-kill algorithm to find the next cell to visit

    Parameters:
        main_grid -- a 2d list of Cell objects as the main maze grid
        visited_status -- a 2d list log visited status of each cell
        current_cell -- Cell object, as the position of the current cell
        grid_width -- the width of the maze

    Returns:
        None if it's deadend
        the Cell of next move
    '''
    
    # Hunting Phase, find unvisited neighbours
    unvisited_neiggbours = []
    
    # exploring 4 directions from the current position
    for move in MOVING_DIRECTIONS:
        neighbour_x = current_cell.x + move[0]
        neighbour_y = current_cell.y + move[1]
        
        if ((0 <= neighbour_x < grid_width) and (0 <= neighbour_y < grid_width) 
            and (visited_status[neighbour_x][neighbour_y] == False)):
            
            unvisited_neiggbours.append((neighbour_x, neighbour_y))
            
    # Killing Phase, carving passages from a random one of the unvisited neighbours
    if len(unvisited_neiggbours) > 0:
        (next_x, next_y) = choice(unvisited_neiggbours)
        return main_grid[next_x][next_y]
    else:  
        return



def find_next_start(grid_width:int, visited_status:list, main_grid:list) -> tuple or None:
    '''
    Function -- find_next_start
        go for the next cell that hasn't been visited, and it has at least one visited neighbour

    Parameters:
        grid_width -- the width of the maze
        visited_status -- a 2d list log visited status of each cell
        main_grid -- a 2d list of Cell objects as the main maze grid

    Returns:
        None, if there isn't any position for a new start
        a tuple of the Cells in the format of (next_cell, from_neighbour)
    '''
    # randomly pick the next start position
    for row in range(grid_width):
            for col in range(grid_width):
                possible_neighbour = has_visited_neighbours(main_grid[row][col], visited_status, grid_width)
                if((visited_status[row][col] == False) and
                   (possible_neighbour)):
                    return (main_grid[row][col], main_grid[possible_neighbour[0]][possible_neighbour[1]])
    return          
                    
                    

def has_visited_neighbours(current_cell:cell.Cell, visited_status:list, grid_width:int) -> None or tuple:
    '''
        Function -- has_visited_neighbours 
            Helper method to check whether there is at least one visited neighbour around the given position

        Parameters:
            x -- x coordinate of current position
            y -- y coordinate of current position

        Returns:
            the neighbour's coordinate if found one
            return None if not
        '''
    for move in MOVING_DIRECTIONS:
        neighbour_x = current_cell.x + move[0]
        neighbour_y = current_cell.y + move[1]
        if((0 <= neighbour_x < grid_width) and 
            (0 <= neighbour_y < grid_width) and 
            (visited_status[neighbour_x][neighbour_y] == True)):
            return (neighbour_x, neighbour_y)
    
    return
            



    