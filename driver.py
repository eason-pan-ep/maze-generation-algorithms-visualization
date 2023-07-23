import hunt_and_kill_algo as hka
from tkinter import *

def main():
    root = Tk()
    root.title("Hunt-and-Kill Visualization")
    root.geometry("500x500")
    
    global output_label
    output_label = Label(root)
    output_label.grid(row=3, column=0, columnspan=10)
    
    
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
    
    hunt_button = Button(root, text="Start Hunting", command=run_hunt_and_kill)
    hunt_button.grid(row=2, column=0, pady=30, columnspan=5)
    
    
    root.mainloop()
    


def hunt_and_kill_visualization() -> None:
    CELL_SIZE = 10
    PLAY_SPEED = 30
    
    grid_size = int(grid_size_input.get())
    start_pos = (int(x_input.get()), int(y_input.get()))
    
    new_window = Toplevel()
    maze = Canvas(new_window, width=(grid_size * CELL_SIZE), height=(grid_size * CELL_SIZE))
    maze.pack()
    hunter = hka.HuntAndKillAlgorithm(grid_size, start_pos)
    
    
    
    new_window.mainloop()

    
def run_hunt_and_kill() -> None:
    '''
    Function -- run_hunt_and_kill 
        test funtion to print the result on the root window
    '''
    grid_size = int(grid_size_input.get())
    start_pos = (int(x_input.get()), int(y_input.get()))
    hunter = hka.HuntAndKillAlgorithm(grid_size, start_pos)
    content = ""
    
    content += ("Initial grid, starting from (%d ,%d):\n" % (start_pos))
    for row in range(len(hunter.grid)):
        for col in range(len(hunter.grid[0])):
            content += ("%d, " % (hunter.grid[row][col]))
        content += "\n"
    content += ("================================\n")
    
    content += ("Running hunt-and-kill......\n")
    hunter.hunt_and_kill()
    content += ("--------[Complete]--------\n")
    content += ("Grid:\n")
    for row in range(len(hunter.grid)):
        for col in range(len(hunter.grid[0])):
            content += ("%d, " % (hunter.grid[row][col]))
        content += "\n"
    content += ("================================\n")
    
    output_label.config(text=content)

if __name__ == "__main__":
    main()