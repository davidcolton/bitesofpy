# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


def _complements_dictionary(str_table):
    complements_dist = dict()
    lines = [line.strip() for line in str_table.split("\n") if line != ""]
    for line in lines[2:]:
        first, *_, last = line.split()
        complements_dist[first.upper()] = last.upper()
    return complements_dist


# Recommended helper function
def _clean_sequence(sequence, str_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    comp_dict = _complements_dictionary(str_table)
    return "".join(
        [char.upper() for char in sequence if char.upper() in comp_dict.keys()]
    )


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    return _clean_sequence(sequence, str_table)[::-1]


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    comp_dict = _complements_dictionary(str_table)
    clean_seq = _clean_sequence(sequence, str_table)
    return "".join([comp_dict[c] for c in clean_seq])


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    return complement(sequence, str_table)[::-1]
