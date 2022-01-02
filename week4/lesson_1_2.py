"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.2 from week 4.
30 December 2021 - Bahadir Arslan
"""

from pathlib import Path
import random
import sys


sys.path.append(str(Path(__file__).parent.parent))
from week3.lesson_1_3 import score
from week3.lesson_1_4 import profile_most_probable_pattern
from week4.lesson_1_1 import profile_with_pseudo_codes


def motifs(profile: dict, k:int, dna: str) -> list:

    list_of_motifs = []
    for string in dna:
        list_of_motifs.append(profile_most_probable_pattern(string, k, profile))
    return list_of_motifs

def random_motifs(dna: str, k: int) -> list:
    
    length = len(dna[0])
    list_of_motifs = []
    for string in dna:
        r = random.randint(0, length-k)
        list_of_motifs.append(string[r:r+k])

    return list_of_motifs


def randomized_motif_search(dna: str, k: int):
    
    best_motifs = random_motifs(dna, k)
    while True:
        profile = profile_with_pseudo_codes(best_motifs)
        list_of_motifs = motifs(profile, k, dna)
        if score(list_of_motifs) < score(best_motifs):
            best_motifs = list_of_motifs
            continue
        break
    return best_motifs
