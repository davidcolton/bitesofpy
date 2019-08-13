IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    count = 0
    for name in names:
        if count == MAX_NAMES or str(name).startswith(QUIT_CHAR):
            break
        elif any(char.isdigit() for char in name) or str(name).startswith(IGNORE_CHAR):
            continue
        else:
            count += 1
            yield name        