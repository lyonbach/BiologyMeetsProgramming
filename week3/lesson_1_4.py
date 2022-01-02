"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.4 from week 3.
27 December 2021 - Bahadir Arslan
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from week3.lesson_1_3 import score, profile

def pr(string: str, profile: dict) -> float:

    """
    Takes consensus and profile as input and returns the probability.
    """

    probability = 1
    for col, char in enumerate(string):
        probability *= profile[char][col]
    return probability

def profile_most_probable_pattern(string: str, length: int, profile: dict) -> str:

    """
    From a given string, returns the most probable k-mer of size length.
    """

    str_length = len(string)
    p_max = float("-inf")
    kmer_p_max = None
    for i in range(str_length - length + 1):
        k_mer = string[i: i+length]
        p = pr(k_mer, profile)
        if p > p_max:
            p_max = p
            kmer_p_max = k_mer
    return kmer_p_max

def greedy_motif_search(dna: list, k: int, t: int):

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
            p = profile(motifs[:j])
            motifs.append(profile_most_probable_pattern(dna[j], k, p))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs
