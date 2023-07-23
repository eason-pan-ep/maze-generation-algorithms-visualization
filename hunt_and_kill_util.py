from random import choice
import cell

global MOVING_DIRECTIONS  # 4 possible moving direction, up, down, left, right
MOVING_DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def hunt_and_kill(main_grid:list, visited_status:list, current_cell:cell.Cell, grid_width:int) -> cell.Cell | None:
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
        # visited_status[next_x][next_y] = True
        # visited_count[0] += 1
        return main_grid[next_x][next_y]
    else:  
        return



def find_next_start(grid_width:int, visited_status:list, main_grid:list) -> cell.Cell | None:
    # randomly pick the next start position
    for row in range(grid_width):
            for col in range(grid_width):
                if((visited_status[row][col] == False) and
                   (has_visited_neighbours(main_grid[row][col], visited_status, grid_width))):
                    # visited_status[row][col] = True
                    # visited_count[0] += 1
                    return main_grid[row][col]     
    return          
                    
                    

def has_visited_neighbours(current_cell:cell.Cell, visited_status:list, grid_width:int) -> bool:
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
        neighbour_x = current_cell.x + move[0]
        neighbour_y = current_cell.y + move[1]
        if((0 <= neighbour_x < grid_width) and 
            (0 <= neighbour_y < grid_width) and 
            (visited_status[neighbour_x][neighbour_y] == True)):
            return True
    
    return False
            





    