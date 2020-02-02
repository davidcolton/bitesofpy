from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    base_letters = Counter(sequence.upper())
    base_a = base_letters["A"]
    base_g = base_letters["G"]
    base_c = base_letters["C"]
    base_t = base_letters["T"]
    base_total = sum([base_a, base_c, base_g, base_t])
    return round(((base_c + base_g) / base_total) * 100, 2)
