"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.3 from week 2.
24 December 2021 - Bahadir Arslan
"""


def faster_symbol_array(genome, symbol):

    array = {}
    n = len(genome)
    extended_genome = genome + genome[0: n//2]
    array[0] = pattern_count(symbol, genome[:n//2])
    previous_first_symbol = genome[0]
    previous_last_symbol = genome[-1]

    for i in range(1, n):
        array[i] = array[i-1] + int(previous_last_symbol == symbol) - int(previous_first_symbol == symbol)
        previous_first_symbol = extended_genome[i]
        previous_last_symbol = extended_genome[i+(n//2)]
    return array        

def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0: n//2]
    for i in range(n):
        array[i] = pattern_count(symbol, extended_genome[i:i+(n//2)])
    return array

def pattern_count(symbol, string):

    return string.count(symbol)
