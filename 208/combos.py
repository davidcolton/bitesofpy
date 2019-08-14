from itertools import combinations

def find_number_pairs(numbers, N=10):
    combs = list(combinations(numbers, 2))
    pairs = []
    for comb in combs:
        if comb[0] + comb[1] == N:
            pairs.append(comb)
    return pairs