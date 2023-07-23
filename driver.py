import hunt_and_kill_algo as hka
from tkinter import *

def main():
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
    
    position_x_input = Entry(root, width=5)
    position_x_input.grid(row=1, column=2)
    
    y_label_input = Label(root, text="Y:")
    y_label_input.grid(row=1, column=3)
    
    position_y = Entry(root, width=5)
    position_y.grid(row=1, column=4)
    
    hunt_button = Button(root, text="Start Hunting", command=run_hunt_and_kill(grid_size, position_x, position_y))
    hunt_button.grid(row=2, column=0, pady=30, columnspan=5)
    
    
    root.mainloop()
    
def run_hunt_and_kill(grid_size:int, x:int, y:int) -> None:
    start_pos = (x, y)
    hunter = hka.HuntAndKillAlgorithm(grid_size, start_pos)
    
    print("Initial grid, starting from (%d ,%d):" % (start_pos))
    for row in hunter.grid:
        print(row)
    print("================================")
    
    print("Initial visited Log:")
    for row in hunter.visited:
        print(row)
    print("================================")
    
    print("Running hunt-and-kill......")
    hunter.hunt_and_kill()
    print("--------[Complete]--------")
    print("Grid:")
    for row in hunter.grid:
        print(row)
    print("-------------------------")
    print("Visited log:")
    for row in hunter.visited:
        print(row)
    print("================================")

if __name__ == "__main__":
    main()