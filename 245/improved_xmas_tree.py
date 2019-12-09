STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    xmas_tree = ""
    max_size = int((rows * 2) - 1)

    # Add the Star
    xmas_tree += f"{STAR:^{max_size}}\n"

    # Add the leaves
    for n in range(1, max_size + 1, 2):
        xmas_tree += f"{n * LEAF:^{max_size}}\n"

    # Add the trunk
    trunk_chars = TRUNK * (rows)
    if rows % 2 == 0:
        trunk_chars += TRUNK
    xmas_tree += f"{trunk_chars:^{max_size}}\n"
    xmas_tree += f"{trunk_chars:^{max_size}}"

    return xmas_tree


print(generate_improved_xmas_tree(20))
