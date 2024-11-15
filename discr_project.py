matrix = [
    ["0", "1", "1", "1", "0"],
    ["0", "0", "1", "1", "0"],
    ["0", "1", "0", "1", "1"],
    ["0", "1", "0", "1", "0"],
    ["0", "1", "1", "1", "1"]
]
def find_in_width(matrix: list[list], start_coord, finish_coord):
    queue = [(start_coord, [(start_coord)])]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [start_coord]
    while True:
        coords, path = queue.pop(0)
        x, y = coords
        for dir_x, dir_y in directions:
            new_x = dir_x + x
            new_y = dir_y + y

            is_x_path = new_x >= 0 and new_x<len(matrix[0])
            is_y_path = new_y >= 0 and new_y<len(matrix)
            if is_x_path and is_y_path and matrix[new_y][new_x] != "0" and (new_x, new_y) not in visited:
                new_path = path[:] + [(new_x, new_y)]
                if (new_x, new_y) == finish_coord:
                    return new_path
                visited.append((new_x, new_y))
                queue.append(((new_x, new_y), new_path))
