"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.1 from week 4.
27 December 2021 - Bahadir Arslan
"""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from week3.lesson_1_4 import profile_most_probable_pattern
from week3.lesson_1_3 import score

def count_with_pseudo_codes(motifs: list) -> dict:

    """
    Takes list of strings and returns a dictionary keys are nucleotides values are count of nucleotides in each row.
    This function initializes counts as 1 to avoid having zero count of any nucleotide.
    """

    length = len(motifs[0])  # Assume all motifs are same length.
    counts = {char: [1]*length for char in "ACGT"}

    for j in range(length):           # Columns
        for i in range(len(motifs)):  # Rows
            char = motifs[i][j]
            counts[char][j] += 1
    return counts

def profile_with_pseudo_codes(motifs: list) -> dict:

    counts = count_with_pseudo_codes(motifs)
    row_count = len(motifs) + 4  # From all nucleotides
    return {char: [value / row_count for value in values] for char, values in counts.items()}

def greedy_motif_search_with_pseudo_counts(dna: str, k: int, t: int) -> dict:

    """
    Finds the set of motifs across a number of DNA sequences that match each other  most closely.
    """

    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][:k])
        pass

    n = len(dna[0])
    for i in range(n-k+1):
        motifs = []
        motifs.append(dna[0][i:i+k])
        for j in range(1, t):
            p = profile_with_pseudo_codes(motifs[:j])
            motifs.append(profile_most_probable_pattern(dna[j], k, p))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs
