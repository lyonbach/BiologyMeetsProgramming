"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.3 from week 3.
26 December 2021 - Bahadir Arslan
"""

import numpy as np
from numpy.core.defchararray import chararray


def count(motifs: list) -> dict:

    """
    Takes list of strings and returns a dictionary keys are nucleotides values are count of nucleotides in each row.
    Key count is always four.
    Each value length (len(list)) motif length dependent.
    """

    length = len(motifs[0])  # Assume all motifs are same length.
    counts = {char: [0]*length for char in "ACGT"}

    for j in range(length):           # Columns
        for i in range(len(motifs)):  # Rows
            char = motifs[i][j]
            counts[char][j] += 1
    return counts

def profile(motifs: list) -> dict:

    """
    Takes list of strings and returns a dictionary keys are nucleotides values are profile of nucleotides in each row.
    Key count is always four.
    Each value length (len(list)) motif length dependent.
    """

    length = len(motifs[0])  # Assume all motifs are same length.
    row_count = len(motifs)
    counts = {char: [0]*length for char in "ACGT"}

    for j in range(length):           # Columns
        for i in range(row_count):  # Rows
            char = motifs[i][j]
            counts[char][j] = float("{:.5f}".format(counts[char][j] + 1 / row_count))
    return counts

def consensus(motifs: list) -> str:

    """
    Takes list of strings of same length as input and returns a string built with the most frequent symbols of the each
    column of the matrix that is built with the input strings.
    """

    consensus = ""
    length = len(motifs[0])
    count_mapping = count(motifs)
    for j in range(length):
        m = 0
        frequent_symbol = ""
        for symbol in "ACGT":
            current_count = count_mapping[symbol][j]
            if current_count > m:
                m = current_count
                frequent_symbol = symbol
        consensus += frequent_symbol

    return consensus

def score(motifs: list) -> int:

    """
    Takes list of stirngs and returns an integer representing the sum of symbols that do not match to consensus string
    in the j-th column of motifs matrix
    """

    length = len(motifs[0])
    consensus_string = consensus(motifs)
    
    score = 0
    for motif in motifs:
        for j in range(length):
            score += consensus_string[j] != motif[j]
    return score

def np_count(motifs: list) -> np.ndarray:

    """
    Takes list of strings and returns the n dimentional array representing occurance of the nucleotides..
    Row count is always four representing nucletides.
    Column count is motif length dependent.
    """

    length = len(motifs[0])
    np_motifs = np.chararray((len(motifs), length))
    for i, motif in enumerate(motifs):
        np_motifs[i:] = list(motif)

    counts = {}
    for char in "ACGT":
        counts[char] = list((np_motifs == char.encode('utf-8')).sum(axis=0))
    return counts

def np_profile(motifs: list) -> np.ndarray:

    """
    Takes list of strings and returns the n dimentional array representing profile of the nucleotides.
    Row count is always four representing nucletides.
    Column count is motif length dependent.
    """

    length = len(motifs[0])
    row_count = len(motifs)
    np_motifs = np.chararray((row_count, length))
    for i, motif in enumerate(motifs):
        np_motifs[i:] = list(motif)

    counts = {}
    for char in "ACGT":
        counts[char] = list((np_motifs == char.encode('utf-8')).sum(axis=0) / row_count)
    return counts

def np_consensus(motifs: list) -> str:

    """
    Takes list of strings and returns a string built with the most frequent nucleotides of each columns.
    """

    length = len(motifs[0])
    np_motifs = np.zeros((4, length), dtype=np.int8)
    for motif in motifs:
        for i, char in enumerate("ACGT"):
            ch_array = np.chararray(length, 1)
            ch_array[:] = list(motif)
            np_motifs[i] += ch_array == char.encode("utf-8")

    sums_idx = np.where(np_motifs == np_motifs.max(axis=0), 1, 0)
    consensus = ""

    for j in range(sums_idx.shape[1]):
        for i in range(sums_idx.shape[0]):
            if sums_idx[i, j]:
                consensus += "ACGT"[i]
                break
    return consensus

def np_score(motifs: list) -> int:

    """
    Takes list of stirngs and returns an integer representing the sum of symbols that do not match to consensus string
    in the j-th column of motifs matrix
    """

    length = len(motifs[0])
    np_motifs = np.zeros((4, length), dtype=np.int8)
    for motif in motifs:
        for i, char in enumerate("ACGT"):
            ch_array = np.chararray(length, 1)
            ch_array[:] = list(motif)
            np_motifs[i] += ch_array == char.encode("utf-8")

    sums_idx = np.where(np_motifs == np_motifs.max(axis=0), 1, 0)
    raise NotImplementedError
    # return (-(sums_idx + -1)).any(axis=0)
