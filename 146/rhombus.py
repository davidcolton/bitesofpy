STAR = "*"


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    rhombus = []
    rhombus_range = list(range(1, width + 1, 2))
    rhombus_range += rhombus_range[:-1][::-1]
    for line in rhombus_range:
        rhombus.append(f"{line * STAR:^{width}}")
    return rhombus
