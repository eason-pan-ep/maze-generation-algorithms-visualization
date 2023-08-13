# Maze Generation with Kruskal's Algorithm

## 1. About/Overview

### Program Overview

This repository contains a Python program that utilizes Tkinter to visualize Kruskal's Algorithm for maze generation. The program generates mazes by applying Kruskal's algorithm, producing a labyrinth of interconnected cells represented in a 2D array. Each cell can be either a wall or a passage, and the algorithm's objective is to connect all cells by progressively removing walls between them.

<img src="https://github.com/macarious/Maze-Generaion-with-Kruskal-s-Algorithm/assets/63441014/37949e9c-f4a0-4399-9b76-04d24b0d3ee7" alt="Sample Generated Maze 1" width="200" />
<img src="https://github.com/macarious/Maze-Generaion-with-Kruskal-s-Algorithm/assets/63441014/4201affa-7fef-42af-ab56-96a77106dd56" alt="Sample Generated Maze 2" width="200" />
<img src="https://github.com/macarious/Maze-Generaion-with-Kruskal-s-Algorithm/assets/63441014/1464cb02-4c18-4432-98db-8f0c6a260877" alt="Sample Generated Maze 3" width="200" />

Kruskal's Algorithm starts with a grid of passages and walls. It iteratively removes walls between cells, ensuring that all cells become interconnected. This removal process involves randomly selecting a wall and verifying whether the cells on either side of the wall are already connected. If they are not connected, the wall is removed, and the cells are united. If the cells are already linked, the wall remains intact. This process continues until all cells are interlinked, creating a coherent maze.

### Disjoint Set Data Structure

To facilitate efficient tracking of connected cells, the program employs a disjoint set data structure. This structure is implemented using a collection of trees, forming a forest. Each tree signifies a set of interconnected cells, with each node in the tree representing an individual cell. Nodes maintain a parent pointer that references the parent node. The root node of each tree symbolizes the entire set, with its parent pointer pointing to itself. The disjoint set structure offers two primary operations: find and union. The find operation returns the root node of the tree containing a specific node, while the union operation merges two trees into one by having the root node of one tree point to the root node of the other. The find operation also utilizes path compression to enhance the efficiency of the find function by restricting the height of the tree.

### Maze Visualization

The generated maze is visually presented using Tkinter, with each set of connected cells represented by a unique randomly-generated color. The maze's layout consists of a 2D array, where "1" signifies walls, and "0" denotes passages. User input controls the maze's `width` and `height`, offering customization options for maze generation.

## 2. Maze Generation Process

### Initial State

At the beginning of the maze generation process, all cells are separated by walls, and each cell is considered its own set. This means that no cell is initially connected to any other cell.

![Initial State](https://github.com/macarious/Maze-Generaion-with-Kruskal-s-Algorithm/assets/63441014/6852d2bf-c0d2-4293-93c6-89a2b6e02578)

### Random Wall Selection

The algorithm then proceeds to randomly select a wall cell from the available list of wall cells. These wall cells are the ones that currently separate two adjacent passage cells.

### Union of Sets

For the chosen wall cell, the algorithm performs a `find` operation to identify the sets of the two adjacent passage cells that the wall cell is separating. If the passage cells are part of different sets, the algorithm proceeds to perform a `union` operation, merging the smaller set into the larger set. This effectively connects the two passage cells and removes the wall between them, creating a passage.

### Repeat and Connect Sets

This process of selecting a random wall cell, checking if the adjacent passage cells are in the same set, and performing a union operation continues until only one set remains in the disjoint set data structure. This signifies that all cells are now connected within a single set, and the maze is complete. The visualization of this process can be seen in the generated maze, where cells of the same set are represented by the same color, showing the interconnectedness of the maze's pathways.

![Walls are removed and sets are merged together](https://github.com/macarious/Maze-Generaion-with-Kruskal-s-Algorithm/assets/63441014/e405d73e-14ce-479e-8ee1-80f058d8d13e)

![Final Configuration of Maze](https://github.com/macarious/Maze-Generaion-with-Kruskal-s-Algorithm/assets/63441014/139d5af0-765a-4251-a1bc-e09fc75c7a1f)

By iteratively breaking down barriers and uniting cells, Kruskal's Algorithm creates a complex yet navigable maze with a clear solution path.

## 3. Takeaway

Kruskal's Algorithm finds an unexpected home in maze generation, proving its versatility beyond typical graph applications. This method efficiently connects cells within a maze, creating a network of passages and corridors. In this context, mazes resemble graphs, where cells are nodes and passages are edges. Kruskal's Algorithm configures the connections and disconnections between nodes, producing intricate paths for exploration. We already know that the shortest paths are between adjacent cells; thus the weight of the edges do not need to be sorted, but instead, only the edges between adjacent cells need to be considered. Uniform distances between cells allow for random edge selection, contributing to the algorithm's simplicity. Its time-complexity, O(E log V) and space complexity O(V) are governed by the efficiency of the disjoint set data structure.

## 4. Technologies

This program was built using:
- Python 3.x
- Tkinter library

## 5. System Requirements

The program should work on any system with Python 3.x installed.

## 6. Installation

1. Clone or download the repository to your local machine.
2. Ensure you have the Tkinter module installed, which is typically included in Python installations.

## 7. Usage

1. Open your terminal or command prompt and navigate to the directory where the program is located.
2. The maze's width and height can be adjusted via user input.
3. Run the program using the command: `python maze_generation.py`.
4. The program's GUI window will display the generated maze with interconnected cells and walls, showcasing the progression of Kruskal's Algorithm.

## 8. Known Issues and Limitations

- The maze's appearance and complexity are dependent on the dimensions specified by the user.
- As of now, user customization of the algorithm parameters (e.g., random wall selection) is not provided through the GUI.

## 9. Contributing

If you encounter any issues or have suggestions for improvement, feel free to submit an issue or pull request on the GitHub repository.

## 10. References
Sure! Here are the citations in IEEE format:

[1] V. D. "Kruskal's Algorithm Animation + Maze Generation," LVNGD, Feb. 7, 2022. [Online]. Available: https://lvngd.com/blog/kruskals-algorithm-animation-maze-generation/. [Accessed: Aug. 12, 2023].
<br />
[2] "Maze generation algorithm," Wikipedia, The Free Encyclopedia. [Online]. Available: https://en.wikipedia.org/wiki/Maze_generation_algorithm. [Accessed: Aug. 12, 2023].
<br />
[3] W. D. Pullen, "Think Labyrinth: Maze Algorithms," Astrolog. [Online]. Available: https://www.astrolog.org/labyrnth/algrithm.htm. [Accessed: Aug. 12, 2023].
<br />
[4] "Disjoint Set Data Structures," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/disjoint-set-data-structures/. [Accessed: Aug. 12, 2023].
