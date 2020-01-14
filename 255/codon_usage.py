import os
from urllib.request import urlretrieve
from collections import Counter

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'U's need to be converted to 'T's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()


def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    # Extract the codon from the translation table
    tt_strings = [
        string.strip() for string in translation_table_str.split("\n") if string != ""
    ]
    tt = dict()
    for string in tt_strings:
        tt_key, tt_value = string.split("=")
        if tt_key.strip().startswith("A"):
            tt[tt_key.strip()] = tt_value.strip()
        else:
            tt[tt_key.strip()] = tt_value.strip().replace("T", "U")

    codons = ["".join(c) for c in (zip(tt["Base1"], tt["Base2"], tt["Base3"]))]

    # Split Codons into bases
    codon_bases = [codons[i : i + 16] for i in range(0, len(codons), 16)]

    # Split Codon Bases into groups and transpose for printing
    codon_groups = []
    for group in codon_bases:
        codon_groups.extend([[group[i : i + 4] for i in range(0, len(group), 4)]])

    # Transpose
    codon_groups_transposed = [list(map(list, zip(*group))) for group in codon_groups]

    # Create AAs lookup keyed on the codon
    aa_lookup = {codons[i]: tt["AAs"][i] for i in range(len(codons))}

    # Count the codons of each type and get a total
    codons_counter = Counter()
    for seq in sequences:
        seq = seq.strip()
        for i in range(0, len(seq), 3):
            codons_counter[seq[i : i + 3]] += 1
    total_codons = sum(codons_counter.values())

    # Calculate the frequency of each codon
    codons_frequency = {
        codon: (codons_counter[codon] / total_codons) * 1000 for codon in codons
    }

    # Manually prepare the print string
    header = "|  Codon AA  Freq  Count  " * 4 + "|"
    line_divider = "-" * 105

    print_table = ""
    print_table = f"{header}\n{line_divider}\n"

    for group in codon_groups_transposed:
        for line in group:
            for cod in line:
                print_table += f"|  {cod}:  {aa_lookup[cod]:2} {codons_frequency[cod]:5.1f} {codons_counter[cod]:6}  "
            print_table += "|\n"
        print_table += f"{line_divider}\n"

    return print_table


if __name__ == "__main__":
    print(return_codon_usage_table())
