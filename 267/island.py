# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def detect_edges(l):
    # No edges
    if sum(l) == 0:
        return 0

    # All land
    if sum(l) == len(l):
        return 2

    edges = 0
    on_land = False
    for idx, loc in enumerate(l):
        if loc == 1 and not on_land:
            edges += 1
            on_land = True
            if idx + 1 == len(l):
                edges += 1
        elif loc == 0 and on_land:
            edges += 1
            on_land = False
        elif idx + 1 == len(l) and on_land:
            edges += 1

    return edges


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0

    # Transpose the map
    map_t = list(map(list, zip(*map_)))

    vert_edges = sum(detect_edges(row) for row in map_)
    hor_edges = sum(detect_edges(row) for row in map_t)

    return vert_edges + hor_edges
