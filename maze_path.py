from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description='finds shortest path in a maze')
parser.add_argument('maze', metavar='maze file', type=str,  help='file containing a maze')
args = parser.parse_args()
maze = args.maze


def breadth_first_search(maze: list[list], start_coord, finish_coord):
    queue = [(start_coord, [(start_coord)])]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [start_coord]
    while True:
        coords, path = queue.pop(0)
        x, y = coords
        for dir_x, dir_y in directions:
            new_x = dir_x + x
            new_y = dir_y + y

            is_x_path = 0 <= new_x < len(maze[0])
            is_y_path = 0 <= new_y < len(maze)
            if (is_x_path and is_y_path and maze[new_x][new_y] != "0" and (new_x, new_y) not in
                    visited):
                new_path = path[:] + [(new_x, new_y)]
                if (new_x, new_y) == finish_coord:
                    return new_path
                visited.append((new_x, new_y))
                queue.append(((new_x, new_y), new_path))


def read_maze(filename: str) -> list[list[str]]:
    """
    Get maze from csv file
    :param filename: str, name of file
    :return: list[list[str]], maze as matrix
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip().split(',') for line in file]


if __name__ == "__main__":
    pprint(breadth_first_search(read_maze(maze), (0, 1), (2, 1)))
    # pprint(read_maze("maze.csv"))
