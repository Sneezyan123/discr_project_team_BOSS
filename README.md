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
