# Shortest path in a maze
### Program usage
``$ python3 maze_path.py [use A*] <maze_file>``

using '-a' or '--a_star' you can use A* algorithm

### Description
Mazes represented as 2-dimensional matrixes.
Value "0" is wall.
Value "1" is path.
Value "X" is a starting point.
There are few starting points, that randomly are picked before using
algorithm as starting point and finish point.

By default, uses breadth first search(BFS), optionally can be changed to A*.


### Report

#### ``parse()``
Parses the input from the terminal
#### ``read_file()``
Simply reads the file line by line, removing commas
#### ``extract_maze()``
Gets the start points from all "X"
#### ``print_maze()``
Prints the maze to the terminal. Coloring block as it goes.
Red for start and end
Green for path
Light gray for unexplored cells
Dark gray for walls
#### ``random_points()``
Sets random start and end points from all possible
#### ``main()``
Main function. Clears the screen and calls all other functions