def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    # Calculate mod where rotate > string length
    mod = abs(n) % len(string)  
    print(mod, -mod)
    if n == 0:
        return string
    if n > 0:
        if n < len(string):
            return string[n:] + string[:n]
        else:
            return string[mod:] + string[:mod]

    if n < 0:
        if abs(n) < len(string):
            return string[n:] + string[:n]
        else:
            return string[-mod:] + string[:-mod]      