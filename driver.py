import hunt_and_kill_algo as hka
from tkinter import *
from cell import *

def main():
    global TILE_SIZE
    TILE_SIZE = 50
    
    root = Tk()
    root.title("Hunt-and-Kill Visualization")
    root.geometry("500x500")

    
    grid_size_label = Label(root, text="Grid Size:")
    grid_size_label.grid(row=0, column=0, padx=20, pady=10)
    
    global grid_size_input
    grid_size_input = Entry(root, width="10")
    grid_size_input.grid(row=0, column=1, columnspan=4)
    
    position_label = Label(root, text="Starting Position:")
    position_label.grid(row=1, column=0, padx=20, pady=10)
    
    x_label = Label(root, text="X:")
    x_label.grid(row=1, column=1)
    
    global x_input
    x_input = Entry(root, width=5)
    x_input.grid(row=1, column=2)
    
    y_label_input = Label(root, text="Y:")
    y_label_input.grid(row=1, column=3)
    
    global y_input
    y_input = Entry(root, width=5)
    y_input.grid(row=1, column=4)
    
    hunt_button = Button(root, text="Start Hunting", command=generate_maze)
    hunt_button.grid(row=2, column=0, pady=30, columnspan=5)
    
    
    root.mainloop()

def generate_maze() -> None:
    size = int(grid_size_input.get())
    new_window = Toplevel()
    new_window.geometry("%dx%d" % (size*TILE_SIZE, size*TILE_SIZE))
    
    canvas = Canvas(new_window, width=size*TILE_SIZE, height=size*TILE_SIZE, )
    canvas.pack()
    
    grid = [[Cell(col, row) for row in range(size)] for col in range(size)]
    init_x = int(x_input.get())
    init_y = int(y_input.get())
    current_cell = grid[init_x][init_y]
    
    # draw all cell walls (initialization)
    for row in range(size):
        for col in range(size):
            grid[row][col].draw_walls(canvas, TILE_SIZE)
    
    current_cell.draw_current_status(canvas, TILE_SIZE)
    
    new_window.mainloop()

if __name__ == "__main__":
    main()