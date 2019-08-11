class my_queue():
    def __init__(self, n=5):
        self.queue = []
        self.n = n

    def append(self, data):
        if len(self.queue) == self.n:
            self.queue.pop(0)
        self.queue.append(data)

    def __iter__(self):
        for x in self.queue:
            yield x


if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """