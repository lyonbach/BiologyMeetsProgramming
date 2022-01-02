"""
Coursera: Introduction to Bioinformatics
Module implements requirements of lesson 1.3 from week 1.
25 December 2021 - Bahadir Arslan
"""

from pathlib import Path
import sys

PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))

from week1.lesson_1_2 import pattern_count

def frequency_map(string: str, length: int) -> dict:

    freq_map = {}
    for i in range(len(string) - length + 1):
        pattern = string[i: i + length]
        freq_map[pattern] = pattern_count(string, pattern)
    return freq_map

def frequent_words(string: str, length: str) -> list:

    words = []
    freq_map = frequency_map(string, length)
    max_val = max(freq_map.values())
    for word, count in freq_map.items():
        if count == max_val:
            words.append(word)
    return sorted(words)
