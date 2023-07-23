from tkinter import *
from cell import *
from hunt_and_kill_util import *
import time

def main():
    '''
    Function -- main
        the starting window, allow users to input size of the maze and starting position
    '''
    
    global TILE_SIZE
    global grid_size_input
    global x_input
    global y_input
    
    TILE_SIZE = 50
    
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
    global new_window
    
    # create pop up window using the size of user input as its width and height
    
    grid_width = int(grid_size_input.get())
    cell_count = grid_width * grid_width
    new_window = Toplevel()
    new_window.geometry("%dx%d" % (grid_width*TILE_SIZE, grid_width*TILE_SIZE)) 
    
    canvas = Canvas(new_window, width=grid_width*TILE_SIZE, height=grid_width*TILE_SIZE, )
    canvas.pack()
    
    # initialize the main grid using user input as its size
    main_grid = [[cell.Cell(col, row) for row in range(grid_width)] for col in range(grid_width)]
    visited_status = [[False for row in range(grid_width)] for col in range(grid_width)]
    visited_count = [0]
    
    #initialize the starting position using user input as its coordinate
    init_x = int(x_input.get())
    init_y = int(y_input.get())
    current_cell = main_grid[init_x][init_y]
    
    # draw all cell walls (initialization)
    for row in range(grid_width):
        for col in range(grid_width):
            main_grid[row][col].draw_walls(canvas, TILE_SIZE)
    
    # test run, for 5 iterations
    flag = 5
    while flag > 0:
        # new_window.after(500, draw_current_cell(current_cell, canvas, TILE_SIZE))
        current_cell.draw_current_status(canvas, TILE_SIZE)
        visited_status[current_cell.x][current_cell.y] = True

        current_cell.is_visited == True
        visited_count[0] += 1
        next_move = hunt_and_kill(main_grid, visited_status, current_cell, grid_width)
        if next_move:
            current_cell = next_move
    flag -= 1

    
    
    new_window.mainloop()


if __name__ == "__main__":
    main()