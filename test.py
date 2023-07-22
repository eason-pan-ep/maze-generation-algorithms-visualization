from hunt_and_kill_algo import *

def main():
    '''
    A wild test for methods in the program
    '''
    test_grid_size = 3
    test_body = HuntAndKillAlgorithm(test_grid_size)
    
    # test1 grid initialization
    print("Test Grid Inivialization:")
    print(test_body.grid)
    
    print("Test visited log matrix initialization:")
    print(test_body.visited)
    
    print("Test hunt and kill algorithm explores all cells:")
    test_body.hunt_and_kill()
    print(test_body.grid)
    print(test_body.visited)
    
    
if __name__ == "__main__":
    main()