"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.5 from week 2.
24 December 2021 - Bahadir Arslan
"""


def hamming_distance(p: str, q: str) -> int:

    # Take the length of the shorter string.
    length = len(p) if len(p) < len(q) else len(q)

    # If strings are not equal, set the distance beforhand.
    distance = abs(len(p) - len(q))

    for i in range(length):
        distance += int(not p[i] == q[i])

    return distance


def approximate_pattern_matching(string: str, pattern: str, max_distance: int) -> list:

    pattern_length = len(pattern)
    match_indices = []

    # We crate a slice of length pattern and slide through input string.
    for i in range(len(string) - pattern_length + 1):
        slice_ = string[i:i+pattern_length]
        if hamming_distance(pattern, slice_) > max_distance:
            continue
        match_indices.append(i)
    return match_indices


def approximate_pattern_count(string: str, pattern: str, max_distance: int) -> int:

    return len(approximate_pattern_matching(string, pattern, max_distance))
