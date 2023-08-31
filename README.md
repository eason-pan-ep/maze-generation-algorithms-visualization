# Maze-generation-algorithms-visualization

### Visualizing Prim's, Kruskal's and hunt-and-kill algorithm to generate mazes, coursework for CS5800 - Algorithms

## Goals
- Implement these algorithms that can generate mazes with different sizes
- Implement visualizations of the maze generation and show how a maze is gradually generated

## How to Run
For Hunt-and-kill
- Get to the program's hunt-and-kill directory in the terminal.
- Run `python3 maze_generation_algorithms_visualization.py`.
- Input `maze size` and `starting position`, then click `hunt-and-kill`.
- After running once, you can click the `hunt-and-kill` button again to generate another maze.

For Prim's algorithm (turtle has been imported):
- Go to the `prims` directory.
- Run 'maze.py' in terminal.
- Input an integer (the side length of the square maze the user wants).

For Kruskal's Algorithm:
- Go to the `kruskal` directory.
- Run `main.py`.
- Input `Width` and `Height` when prompted.

## Required Package
Tkinter

## Limitations
- code is not optimized for error prevention and error handling
- Visualization modules work separately in different algorithms
- The program is not designed in the best practice of MVC pattern
