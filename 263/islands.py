from itertools import product
from collections import defaultdict
from collections import deque

# Probably overkill but a little generator to count the islands visited
def island_number():
    island_number = 1
    while True:
        yield island_number
        island_number += 1


# Given a grid position and a grid size return all possible neighbors
def get_neighbors(position, grid_size):
    row, col = position
    north = (row - 1, col)
    east = (row, col + 1)
    south = (row + 1, col)
    west = (row, col - 1)
    neighbors = [north, east, south, west]
    return [
        neighbor
        for neighbor in neighbors
        if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size
    ]


def count_islands(grid):

    # The size of the grid and all possible grid positions
    size_of_grid = len(grid)
    grid_positions_to_visit = list(product(range(size_of_grid), range(size_of_grid)))

    # Island number generator
    islands = island_number()
    number_of_islands = 0

    # Reduce the number of positions to visit to just those that are land
    # This will also catch the scenario of invlaid data
    try:
        land_coordinates = [
            position
            for position in grid_positions_to_visit
            if grid[position[0]][position[1]] == 1
        ]
    except IndexError:
        return number_of_islands

    # While there are more land positions to visit
    while land_coordinates:

        # Set up some variable to track progress
        visited = set()
        neighbors = deque()

        # Get the first position and add to visited
        visiting = land_coordinates[0]
        visited.add(visiting)

        # Create an initial set of neighboring positions
        [neighbors.append(n) for n in get_neighbors(visiting, size_of_grid)]
        while neighbors:
            neighbor = neighbors.popleft()

            # If the neighbor is a land position and I haven't already visited it
            if neighbor in land_coordinates and neighbor not in visited:

                # Add the neighbor to visited and update with neighbors of the neighbor
                visited.add(neighbor)
                [neighbors.append(n) for n in get_neighbors(neighbor, size_of_grid)]

        # All neighbors visited
        # Get the island number and clear out any already visited positions
        number_of_islands = next(islands)
        [land_coordinates.remove(pos) for pos in visited]

    return number_of_islands
