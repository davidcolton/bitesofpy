from collections import namedtuple

RIGHT, DOWN, LEFT, UP = "⇒", "⇓", "⇐", "⇑"
START_VALUE = 1

GridPosition = namedtuple("GridPosition", "line pos")
GridMove = namedtuple("GridMove", "x_move y_move")

MOVE_RIGHT = GridMove(0, 1)
MOVE_DOWN = GridMove(1, 0)
MOVE_LEFT = GridMove(0, -1)
MOVE_UP = GridMove(-1, 0)

grid_moves = {MOVE_RIGHT: RIGHT, MOVE_DOWN: DOWN, MOVE_LEFT: LEFT, MOVE_UP: UP}

small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""


def _create_list_of_lines(grid):
    lol = []
    for line in grid.strip().splitlines():
        if "|" in line:
            continue
        lol.append([int(n) for n in line.replace("-", " ").split()])
    return lol


def _determine_direction(first, second):
    line_diff = second.line - first.line
    pos_diff = second.pos - first.pos
    return grid_moves[GridMove(line_diff, pos_diff)]


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    lol = _create_list_of_lines(grid)
    grid_dict = dict()
    for line in range(len(lol)):
        for pos in range(len(lol)):
            grid_dict[lol[line][pos]] = GridPosition(line, pos)

    # Take first two values and establish direction
    first, second = sorted(grid_dict)[:2]
    move_direction = _determine_direction(grid_dict[first], grid_dict[second])

    # Start the print line
    print_line = f"{str(first)} "

    # Iterate from the 2nd element to the second from last
    for element in sorted(grid_dict)[1:-1]:
        # See if there is a change in direction to the next element
        new_direction = _determine_direction(grid_dict[element], grid_dict[element + 1])
        # No Change
        if new_direction == move_direction:
            print_line += f"{element} "
        # Change
        # Add element and change to print line
        # Update move direction and reset line
        else:
            print_line += f"{element} {new_direction}"
            print(print_line)
            move_direction = new_direction
            print_line = f""

    print(f"{print_line}{max(grid_dict)}")
    """print(
        (grid_dict[6].line - grid_dict[5].line), (grid_dict[6].pos - grid_dict[5].pos)
    )"""


print_sequence_route(small_grid)
