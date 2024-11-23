import argparse
import random
from pprint import pprint
import os

GREEN = '\033[0;32m'
DARK_GRAY = "\033[1;30m"
DEFAULT = '\033[0m'

parser = argparse.ArgumentParser(description='finds shortest path in a maze')
parser.add_argument('maze', metavar='maze_file', type=str, help='file containing a maze')
args = parser.parse_args()
arg_maze = args.maze


def breadth_first_search(maze: list[list[str]], start_coord, finish_coord) -> list[tuple[int, int]]:
    """
    BFS algorithm to find the shortest path in a maze from start_coord to finish_coord
    :param maze: list[list[str]], maze represented by 0 and 1. 0 being the walls
    :param start_coord: tuple[int, int], start coordinate
    :param finish_coord: tuple[int, int], finish coordinate
    :return: list[tuple[int, int]], shortest path from start_coord to finish_coord
    # >>> pprint(breadth_first_search([['0', '1', '1', '1', '0'], ['0', '0', '1', '1', '0'],\
    # ['0', '1', '0', '1', '1'], ['0', '1', '0', '1', '0'], ['0', '1', '1', '1', '1'],\
    # ['0', '1', '0', '0', '0']], (0, 1), (2, 1)))
    >>> maze, points = extract_maze(read_file('maze.csv'))
    >>> points = random_points(points)
    >>> pprint(breadth_first_search(maze, points[0], points[1]))

    """
    queue = [(start_coord, [start_coord])]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [start_coord]
    while True:
        coords, path = queue.pop(0)
        x, y = coords
        for dir_x, dir_y in directions:
            new_x = dir_x + x
            new_y = dir_y + y

            is_x_path = 0 <= new_x < len(maze)
            is_y_path = 0 <= new_y < len(maze[0])
            if (is_x_path and is_y_path and maze[new_x][new_y] != "0" and (new_x, new_y) not in
                    visited):
                new_path = path[:] + [(new_x, new_y)]
                if (new_x, new_y) == finish_coord:
                    return new_path
                visited.append((new_x, new_y))
                queue.append(((new_x, new_y), new_path))


def read_file(filename: str) -> list[list[str]]:
    """
    Get maze from csv file
    :param filename: str, name of file
    :return: list[list[str]], maze as matrix
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode= 'w+', suffix=".txt") as temp_input:
    ...     _ = temp_input.write('0,X,1,1,0\\n'
    ...                     '0,0,1,1,0\\n'
    ...                     '0,X,0,1,1\\n'
    ...                     '0,1,0,1,0\\n'
    ...                     '0,1,1,1,1\\n'
    ...                     '0,1,0,0,0')
    ...     _ = temp_input.seek(0)
    ...     pprint(read_file(temp_input.name))
    [['0', 'X', '1', '1', '0'],
     ['0', '0', '1', '1', '0'],
     ['0', 'X', '0', '1', '1'],
     ['0', '1', '0', '1', '0'],
     ['0', '1', '1', '1', '1'],
     ['0', '1', '0', '0', '0']]
    """
    with (open(filename, 'r', encoding='utf-8') as file):
        return [line.strip().split(',') for line in file]


def extract_maze(maze: list[list[str]]) -> tuple[list[list[str]], list[tuple[int, int]]]:
    """
    Convert maze to zeros and ones, and get the end points
    :param maze: list[list[str]], maze from file
    :return: tuple[list[list[str]], list[tuple[int, int]]],
    >>> pprint(extract_maze([['0', 'X', '1', '1', '0'], ['0', '0', '1', '1', '0'],\
     ['0', 'X', '0', '1', '1'], ['0', '1', '0', '1', '0'], ['0', '1', '1', '1', '1'],\
     ['0', '1', '0', '0', '0']]))
    ([['0', '1', '1', '1', '0'],
      ['0', '0', '1', '1', '0'],
      ['0', '1', '0', '1', '1'],
      ['0', '1', '0', '1', '0'],
      ['0', '1', '1', '1', '1'],
      ['0', '1', '0', '0', '0']],
     [(0, 1), (2, 1)])
    >>> pprint(extract_maze(read_file('maze.csv')))

    """
    points = []
    new_maze = []
    for i, x in enumerate(maze):
        row = []
        for j, y in enumerate(x):
            if y == 'X':
                points.append((i, j))
                row.append('1')
            elif y == '1':
                row.append('1')
            else:
                row.append('0')
        new_maze.append(row)
    return new_maze, points


def print_maze(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """
    Print maze
    :param maze: list[list[str]], maze represented by 0 and 1. 0 being the walls
    :param path: list[tuple[int, int]], shortest path from start_coord to finish_coord
    :return: None
    """
    path = set(path)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join([''.join(f'{GREEN}██{DEFAULT}' if (y, x) in path else
                             f'{DARK_GRAY}██{DEFAULT}' if cell == "1" else '  '
                             for x, cell in enumerate(row)) for y, row in enumerate(maze)]))


def random_points(points: list[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Get to random points from list
    :param points: list[tuple[int, int]], list of possible points
    :return: tuple[tuple[int, int], tuple[int, int]], two points
    """
    if len(points) == 2:
        return points[0], points[1]
    return tuple(random.sample(points, k=2))


def main(file_name: str) -> None:
    """
    Main function
    :param file_name: name of file from which to read maze
    :return: None
    """
    maze, points = extract_maze(read_file(args.maze))
    points = random_points(points)
    path = breadth_first_search(maze, points[0], points[1])
    print_maze(maze, path)


if __name__ == "__main__":
    main(arg_maze)
