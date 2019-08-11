def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = 0
    words = 0
    chars =0
    with open(file_, 'r') as reader:
        line = reader.readline()
        while line != '':
            lines += 1
            words += len(line.split())
            chars += len(line)
            line = reader.readline()
            
    return (f'{lines}\t{words}\t{chars}\t{file_}')