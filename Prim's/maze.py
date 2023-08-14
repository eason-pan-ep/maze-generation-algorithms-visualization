import math
from turtle import *
import time
from prim import Prim

SIDE_LENGTH = 25


class DrawSquareMaze:

    def __init__(self, n=1, sideLen=1):
        self.n = n
        self.sideLen = sideLen
        self.prim = Prim(n)
        self.set_up()

    def set_up(self):
        # Initialize turtle settings
        pensize(2)
        hideturtle()
        speed(0)

    def draw_square(self, side):
        # Draw a square
        for _ in range(4):
            forward(side)
            right(90)

    def draw_cell(self, x, y, node, mst):
        # Draw a cell with gates based on MST
        penup()
        goto(x, y)
        pendown()

        directions = [self.prim.TOP, self.prim.RIGHT,
                      self.prim.BOTTOM, self.prim.LEFT]
        gates = [mst[node][dir] == 1 for dir in directions]

        # Special case for the entrance and exit
        if node == 0:
            gates[3] = True
        elif node == self.n ** 2 - 1:
            gates[1] = True

        for gate in gates:
            if gate:
                penup()
            else:
                pendown()
            forward(self.sideLen)
            right(90)

    def draw_entire_maze(self):
        # Create and draw the entire maze based on Prim's MST
        mst = self.prim.generate_mst()
        startX, startY = self.get_start_coords()

        for row in range(self.n):
            for column in range(self.n):
                node = row * self.n + column
                x = startX + column * self.sideLen
                y = startY - row * self.sideLen
                self.draw_cell(x, y, node, mst)

    def get_start_coords(self):
        # Returns the starting coordinates for the maze drawing
        return (int(- (self.n / 2) * self.sideLen), int((self.n / 2) * self.sideLen))

    def save_screenshot(self):
        # Saves a screenshot of the current turtle window
        ts = getscreen()
        ts.getcanvas().postscript(
            file=f"gallery/{math.floor(time.time())}.eps")


if __name__ == '__main__':
    n = int(input("Please enter the size (square side length) of the maze: "))
    maze_visualization = DrawSquareMaze(n, SIDE_LENGTH)
    maze_visualization.draw_entire_maze()
    done()
