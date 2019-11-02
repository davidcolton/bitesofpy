def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    STAR = "*"
    xmax_tree = ""
    max_size = int((rows * 2) - 1)
    for n in range(1, max_size + 1, 2):
        xmax_tree += f"{n * STAR:^{max_size}}"
        if n < max_size:
            xmax_tree += "\n"
    return xmax_tree


print(generate_xmas_tree(rows=3))
