import hunt_and_kill_algo as hka
from tkinter import *

def main():
    
    global root
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
    
    hunt_button = Button(root, text="Start Hunting", )
    hunt_button.grid(row=2, column=0, pady=30, columnspan=5)
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main()