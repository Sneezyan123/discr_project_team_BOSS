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


def dijkstra_path(adj_list: dict, start_v, end_v) -> list:
    """
    Returns the shortest path from `start_v` to `end_v`

    Args:
        adj_list (dict): adjecency list of format {vertex: [(vertex, weight)]}
        start_v (_type_): vertex
        end_v (_type_): vertex

    >>> dijkstra_path({\
        1: [(2, 2), (3, 5), (4, 10)],\
        2: [(1, 3), (3, 2)],\
        3: [(4, 1)],\
        4: []\
    }, 1, 4)
    [1, 2, 3, 4]
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
    return path






if __name__ == "__main__":
    import doctest
    doctest.testmod()



    print(dijkstra({
        1: [(2, 2), (3, 5), (4, 10)],
        2: [(1, 3), (3, 2)],
        3: [(4, 1)],
        4: []
    }, 1, 4))
