"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.4 from week 2.
24 December 2021 - Bahadir Arslan
"""


def skew_array(genome: str) -> list:
    
    value_mapping = {'A': 0, 'T': 0, 'G': 1, 'C': -1}
    n = len(genome)
    extended_genome = genome + genome[:n//2]

    output_array = [0, ]
    for i in range(0, n):
        output_array.append(output_array[i] + value_mapping[extended_genome[i]])
    return output_array

def minium_skew(genome: str) -> list:

    skewArray = skew_array(genome)
    min_value = min(skewArray)

    positions = []
    for i, value in enumerate(skewArray):
        if value == min_value:
            positions.append(i)
    return positions
