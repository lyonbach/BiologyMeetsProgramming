"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.4 from week 4.
1 January 2022 - Bahadir Arslan
"""

import copy
from pathlib import Path
import random
import sys

sys.path.append(str(Path(__file__).parent.parent))

from week3.lesson_1_3 import score
from week3.lesson_1_4 import pr
from week4.lesson_1_1 import profile_with_pseudo_codes
from week4.lesson_1_2 import random_motifs


def normalize(probabilities: dict) -> dict:

    """
    Takes a dictionary "probabilities" whose keys are k-mers and whose values are the probabilities of these k-mers and
    returns normalized probabilities dictionary.
    """

    sum_of_all_values = sum(list(probabilities.values()))
    return {k:v/sum_of_all_values for k, v in probabilities.items()}


def weighted_die(normalized_probabilities: dict) -> str:

    """
    Takes a dictionary "normalized_probabilities" whose keys are k-mers and whose values are the normalized
    probabilities of these k-mers and returns a randomly chosen k-mer character with respect to the values in probabilities.
    """

    r = random.uniform(0, 1)

    for (k_mer, probability) in normalized_probabilities.items():
        r -= probability
        if r <= 0:
            return k_mer


def profile_generated_string(text: str, profile: dict, k: int) -> str:

    n = len(text)
    probabilities = {}

    for i in range(0, n - k + 1):
        sub = text[i: i + k]
        probabilities[sub] = pr(sub, profile)

    probabilities = normalize(probabilities)
    return weighted_die(probabilities)


def gibbs_sampler(dna: str, k: int, t: int, n: int) -> list:

    """
    Implements gibbs sampler motif search algorithm using pseudocount.
    :k: Motif length.
    :t: Motif count.
    :n: Iteration count.
    """

    motifs = random_motifs(dna, k)
    best_motifs = copy.copy(motifs)  # Init best motifs as randomly selected motifs.
    for _ in range(n):
        r = random.randint(0, t)
        rth_string = motifs.pop(r - 1)  # Zero based indexing.
        profile = profile_with_pseudo_codes(motifs)
        motifs.insert(r, profile_generated_string(rth_string, profile, k))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs
