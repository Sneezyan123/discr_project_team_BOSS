# Shortest path in a maze
### Program usage
```Bash
$ python3 maze_path.py [use A*] <maze_file>
```

using '-a' or '--a_star' you can use A* algorithm

### Description
Mazes represented as 2-dimensional matrixes.
* Value "0" is wall.
* Value "1" is path.
* Value "X" is a starting point.

There are few starting points, that randomly are picked before using
algorithm as starting point and finish point.

By default, uses breadth first search(BFS), optionally can be changed to A*.

## A* Algorithm
> Mykyta Yagoda

The algorithm is similar to BFS, but gives priorities to each node: how far this node is from the finish_node and how short the path to current vertex is. "How far from the finish_node" is called heuristic(h) and it does not take into account obstacles

$ h = |x_i - x_f| + |y_i - y_f| $

where $x_i, y_i$ -- coordinates of the current node

$x_f, y_f$ -- coordinates of the finish node

When picking next node we choose the one with the best priority among all in queue.
The queue itself stores: priority, coordinates of the node, path from the starting node to it.

![alt text](image.png)