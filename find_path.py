from queue import PriorityQueue


def dijkstra(adj_list: dict, start_v, end_v) -> float:
    """
    Returns the length of shortest path from `start_v` to `end_v`

    Args:
        adj_list (dict): adjecency list of format {vertex: [(vertex, weight)]}
        start_v (_type_): vertex
        end_v (_type_): vertex

    >>> dijkstra({\
        1: [(2, 2), (3, 5), (4, 10)],\
        2: [(1, 3), (3, 2)],\
        3: [(4, 1)],\
        4: []\
    }, 1, 4)
    5
    """
    p_queue = PriorityQueue()
    dist = {key: float("inf") for key in adj_list}

    dist[start_v] = 0
    p_queue.put((0, start_v))

    while not p_queue.empty():
        d, v = p_queue.get()
        # print(d, v)
        if v == end_v:
            return d

        for v_to, d_to in adj_list[v]:
            dist_from_start_to = d+d_to
            if dist_from_start_to < dist[v_to]:
                dist[v_to] = dist_from_start_to
                p_queue.put((dist_from_start_to, v_to))
    return dist[end_v]


def dijkstra_path(adj_list: dict, start_v, end_v) -> tuple[int, list]:
    """
    Returns the shortest distance and path from `start_v` to `end_v`

    Args:
        adj_list (dict): adjecency list of format {vertex: [(vertex, weight)]}
        start_v (_type_): vertex
        end_v (_type_): vertex

    Return:
        shortest_distance path (tuple[int, list])

    >>> dijkstra_path({\
        1: [(2, 2), (3, 5), (4, 10)],\
        2: [(1, 3), (3, 2)],\
        3: [(4, 1)],\
        4: []\
    }, 1, 4)
    (5, [1, 2, 3, 4])
    """
    p_queue = PriorityQueue()
    dist = {key: (float("inf"), None) for key in adj_list}

    dist[start_v] = (0, None)
    p_queue.put((0, start_v))

    while not p_queue.empty():
        d, v = p_queue.get()
        # print(d, v)
        if v == end_v:
            break

        for v_to, d_to in adj_list[v]:
            dist_from_start_to = d+d_to
            if dist_from_start_to < dist[v_to][0]:
                dist[v_to] = (dist_from_start_to, v)
                p_queue.put((dist_from_start_to, v_to))

    #get_path
    shortest_distance, prev_v = dist[end_v]
    path = [end_v]
    while prev_v is not None:
        path.append(prev_v)
        prev_v = dist[prev_v][1]

    path = path[-1::-1]
    return shortest_distance, path


def A_star(maze: list[list[str]], \
    start_coord: tuple[int, int], finish_coord: tuple[int, int]) -> list[tuple[int, int]]:
    """
    A* algorithm

    :param maze: list[list[str]], maze represented by 0 and 1. 0 being the walls
    :param start_coord: tuple[int, int], start coordinate
    :param finish_coord: tuple[int, int], finish coordinat
    """
    n = len(maze)
    m = len(maze[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = PriorityQueue()
    #sum of distance from starting node and distance to finish node
    q.put((0, start_coord, [start_coord]))
    visited = []
    while not q.empty():
        _, coord, path = q.get()
        if coord == finish_coord:
            return path

        if coord in visited:
            continue
        visited.append(coord)

        for d in directions:
            new_coord = (coord[0] + d[0], coord[1] + d[1])
            if 0 <= new_coord[0] < n and 0 <= new_coord[1] < m:
                if maze[new_coord[0]][new_coord[1]] != "1":
                    continue
                dist_start = (new_coord[0]-start_coord[0])**2 + (new_coord[1]-start_coord[1])**2
                dist_finish = (new_coord[0]-finish_coord[0])**2 + (new_coord[1]-finish_coord[1])**2
                new_path = path[:]
                new_path.append(new_coord)

                q.put((dist_start+dist_finish, new_coord, new_path))

    return None



if __name__ == "__main__":
    import doctest
    doctest.testmod()



    print(dijkstra({
        1: [(2, 2), (3, 5), (4, 10)],
        2: [(1, 3), (3, 2)],
        3: [(4, 1)],
        4: []
    }, 1, 4))

    print(A_star([['0', '1', '1', '1', '0'],
                  ['0', '0', '1', '1', '0'],
                  ['0', '1', '0', '1', '1'],
                  ['0', '1', '0', '1', '0'],
                  ['0', '1', '1', '1', '1'],
                  ['0', '1', '0', '0', '0']],
        (0, 1), (2, 1)))
