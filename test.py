from hunt_and_kill_algo import *

def main():
    '''
    A wild test for methods in the program
    '''
    test_grid_size = 6
    starting_position = (5, 2)
    test_body = HuntAndKillAlgorithm(test_grid_size, starting_position)
    
    # test1 grid initialization
    print("Initial grid, starting from (%d ,%d):" % (starting_position))
    for row in test_body.grid:
        print(row)
    print("================================")
    
    print("Initial visited Log:")
    for row in test_body.visited:
        print(row)
    print("================================")
    
    print("Running hunt-and-kill......")
    test_body.hunt_and_kill()
    print("--------[Complete]--------")
    print("Grid:")
    for row in test_body.grid:
        print(row)
    print("-------------------------")
    print("Visited log:")
    for row in test_body.visited:
        print(row)
    print("================================")
    
    
if __name__ == "__main__":
    main()