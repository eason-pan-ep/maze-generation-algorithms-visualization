from tkinter import *
from cell import *
import hunt_and_kill_util as hak

def main() -> None:
    '''
    Function -- main
        the starting window, allow users to input size of the maze and starting position
        the algorithm works for maze size from 1x1 to Max_Int value
        for best visualization please use maze size from 1x1 to 50x50
    '''

    global grid_size_input, x_input, y_input
    
    root = Tk()
    root.title("Hunt-and-Kill Visualization")
    root.geometry("500x500")
    
    grid_size_label = Label(root, text="Grid Size:")
    grid_size_label.grid(row=0, column=0, padx=20, pady=10)
    
    grid_size_input = Entry(root, width="10")
    grid_size_input.grid(row=0, column=1, columnspan=4)
    
    position_label = Label(root, text="Starting Position:")
    position_label.grid(row=1, column=0, padx=20, pady=10)
    
    x_label = Label(root, text="X:")
    x_label.grid(row=1, column=1)  
    
    x_input = Entry(root, width=5)
    x_input.grid(row=1, column=2)
    
    y_label_input = Label(root, text="Y:")
    y_label_input.grid(row=1, column=3)
    
    y_input = Entry(root, width=5)
    y_input.grid(row=1, column=4)
    
    hunt_button = Button(root, text="Start Hunting", command=generate_maze)
    hunt_button.grid(row=2, column=0, pady=30, columnspan=5)
    
    
    root.mainloop()
    
    

def generate_maze() -> None:
    '''
    Function -- generate_maze
        the visualization window
    '''
    
    global tile_size, interval_time, wall_thickness, new_window
    
    wall_thickness = 3
    tile_size = 50
    interval_time = 100
    
    # create pop up window using the size of user input as its width and height
    new_config = running_config()
    if new_config:
        tile_size = new_config[0]
        interval_time = new_config[1]
        wall_thickness = new_config[2]
    
    grid_width = int(grid_size_input.get())
    cell_count = grid_width * grid_width
    new_window = Toplevel()
    new_window.geometry("%dx%d" % (grid_width*tile_size, grid_width*tile_size)) 
    
    # initialize the canvas for displaying the maze
    canvas = Canvas(new_window, width=grid_width*tile_size, height=grid_width*tile_size, background="#2B2B2B")
    canvas.pack()
    
    # initialize the main grid using user input as its size
    main_grid = [[Cell(col, row, wall_thickness) for row in range(grid_width)] for col in range(grid_width)]
    visited_status = [[False for row in range(grid_width)] for col in range(grid_width)]
    visited_count = [0]
    
    #initialize the starting position using user input as its coordinate
    init_x = int(x_input.get())
    init_y = int(y_input.get())
    current_cell = main_grid[init_x][init_y]
    current_cell.draw_current_status(canvas, tile_size)
    
    # draw all cell walls (initialization)
    for row in range(grid_width):
        for col in range(grid_width):
            main_grid[row][col].draw_walls(canvas, tile_size)

    while visited_count[0] < cell_count:
        wait_interval()
        
        visited_status[current_cell.x][current_cell.y] = True
        current_cell.is_visited = True
        visited_count[0] += 1
        
        next_move = hak.hunt_and_kill(main_grid, visited_status, current_cell, grid_width)
        if next_move:  # running hunt-and-kill until it reaches to a deadend
            current_cell.draw_path(canvas, tile_size)
            remove_walls(current_cell, next_move)
            current_cell.draw_walls(canvas, tile_size)
            next_move.draw_walls(canvas, tile_size)
            current_cell = next_move
            current_cell.draw_current_status(canvas, tile_size)
        else:  # when reaching to a deadend, go and randomly find the next starting position
            next_move = hak.find_next_start(grid_width, visited_status, main_grid)
            if next_move:
                current_cell.draw_path(canvas, tile_size)
                remove_walls(current_cell, next_move)
                current_cell.draw_walls(canvas, tile_size)
                next_move.draw_walls(canvas, tile_size)
                current_cell = next_move
                current_cell.draw_current_status(canvas, tile_size)
            else:
                break
    
    # draw the last cell       
    current_cell.draw_path(canvas, tile_size)
    current_cell.draw_walls(canvas, tile_size)
    
    
    new_window.mainloop()
    


def running_config() -> list | None:
    '''
    Function -- running_config
        config the maze UI to fit the screen
        for the best visualization experience, please use 1 <= size < 50

    Returns:
        1 <= sise < 20 using default
        otherwise, return a list [new_tile_size, new_interval, new_thickness]
    '''
    
    input_size = int(grid_size_input.get())
    if input_size // 10 <= 1:
        return
    elif interval_time == 0:  # reserved for quick demo purposes
        return
    else:
        balancer = input_size // 10
        
        return (round(tile_size / (1.01 * balancer)), round(interval_time / (4 * balancer)), round(wall_thickness / (0.8 * balancer)))
    
   

def wait_interval() -> None:
    '''
    Function -- wait_interval 
        have the maze generation animation with certain time interval
    '''
    var = tkinter.IntVar()
    new_window.after(interval_time, var.set, 1)
    new_window.wait_variable(var)



def remove_walls(current_cell:Cell, next_cell:Cell) -> None:
    '''
    Function -- remove_walls 

    Parameters:
        current_cell -- Cell object, current cell
        next_cell -- Cell object, the cell moving towards
    '''
    
    diff_x = current_cell.x - next_cell.x
    diff_y = current_cell.y - next_cell.y
    
    if diff_x == 1:
        current_cell.walls["left"] = False
        next_cell.walls["right"] = False
    if diff_x == -1:
        current_cell.walls["right"] = False
        next_cell.walls["left"] = False
    if diff_y == 1:
        current_cell.walls["top"] = False
        next_cell.walls["bottom"] = False
    if diff_y == -1:
        current_cell.walls["bottom"] = False
        next_cell.walls["top"] = False

    


if __name__ == "__main__":
    main()
    
    
    