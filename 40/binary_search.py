def binary_search(sequence, target):
    def _recursive_binary_search(start, end, seq, target):
        # Start & end are used to track the original
        #    start index of the sequence - initially 0
        #    end index of the sequence - initially len(seq) -1

        # The length of the sequence and the step size
        length = len(seq)
        step = length // 2

        # Two stopping scenarios
        # The length of the sequence is now either 1 or 2
        if length == 2:
            if seq[0] == target:
                return start
            if seq[1] == target:
                return end
            else:
                return None
        if length == 1:
            if seq[step] == target:
                return start
            else:
                return None

        if seq[step] > target:
            return _recursive_binary_search(start, start + step, seq[:step], target)
        else:
            return _recursive_binary_search(start + step, end, seq[step:], target)

    return _recursive_binary_search(0, len(sequence) - 1, sequence, target)


print(
    binary_search(
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61], 61
    )
)

