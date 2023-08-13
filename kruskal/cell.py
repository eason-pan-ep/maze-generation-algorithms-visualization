'''
class Cell
Description: This class represents a cell in the maze.
'''


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other_cell):
        return self.x == other_cell.x and self.y == other_cell.y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
