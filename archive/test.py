from archive.hunt_and_kill_algo import *

def main():
    '''
    A wild test for methods in the program
    '''
    grid_size = 10
    starting_position = (2, 4)
    hunter = HuntAndKillAlgorithm(grid_size, starting_position)
    
    print("Initial grid, starting from (%d ,%d):" % (starting_position))
    for row in hunter.grid:
        print(row)
    print("================================")
    
    hunter.hunt_and_kill()
    print("End")
    
        
 
    
    
if __name__ == "__main__":
    main()