# Visualization Documentation

## Table of Content
- Part 1 - General Program Structure
- Part 2 - Visualization Logics & Functions

## Part 1 - General Program Structure
### Overview
The whole program contains function-based Python files, except the `cell.py`.

`cell.py` is the the Class representing Cell objects used in the visualization. Cell objects are instantiated when the main grid of maze is initialized. And manipulating some of its fields during the visualization process.

### Seperated Algorithm files and the visualizations
The main algorithm files are better be seperated, except the parts that involve visualizations, like the rendering sequence based on specific algorithm features. 

> For instance, the hunt-and-kill algorithm finds a unvisited but adjacent cell to start when it hits a dead-end. The sequence of rendering these steps are included in the `maze_generation_algorithms_visualization.py`. However, the main logic of the algorithm, like how it chooses the running directions and how to find the next start point should be included in a seperated Python file, in this example, they are included in `hunt_and_kill_util.py`.

## Part 2 - Visualization Logics & Functions
The main challenge to visualize maze generations are rendering walls during the algorithm running. To solve it, the methods used are listed below.
### Render the Head
For better visualization, we can highlight the head of a path when it's generating. To do so, simply call the method in Cell `cell_name.draw_current_status(canvas, tile_size)`

### Draw Cell Walls
Considering each cell as a tile but not a dot is the first intuition for this visualization. And each tile has 4 walls `Top, Down, Left, Right`. 
![Figure 1 - illustration of cell as a tile concept](./documentation_imgs/figure_1.png)

To render walls of a cell, call the function(method) in Cell, `cell_name.draw_walls(canvas, tile_size)`. The method draws walls depending on their status. The wall rendering won't update automatically when you remove a wall; Thus, you would always want to draw walls again after removing or adding walls to a cell.

### Remove Walls



