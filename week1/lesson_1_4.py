"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.4 from week 1.
25 December 2021 - Bahadir Arslan
"""

def reverse(pattern: str) -> str:

    reversed_pattern = ''
    while pattern:
        reversed_pattern += pattern[-1]
        pattern = pattern[:-1]
    return reversed_pattern

def complement(pattern: str) -> str:

    complementary = ''
    nucleotide_mapping = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

    for char in pattern:
        complementary += nucleotide_mapping[char]

    return complementary

def reverse_complement(pattern: str) -> str:

    return reverse(complement(pattern))

def pattern_matching(pattern: str, string: str) -> list:

    matches = []
    length = len(pattern)
    for i in range(len(string) - length + 1):
        if pattern != string[i: i + length]:
            continue
        matches.append(i)
    return matches
