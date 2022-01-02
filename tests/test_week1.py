from pathlib import Path
import sys
import unittest


PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))

from week1.lesson_1_2 import pattern_count
from week1.lesson_1_3 import frequency_map, frequent_words
from week1.lesson_1_4 import complement, reverse, reverse_complement, pattern_matching

import common


class TestLesson_1_2(unittest.TestCase):

    def test_pattern_count(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "PatternCount.txt"
        test_data = common.retrieve_test_data(file_path)
        for (string, pattern), expected in test_data:
            result = pattern_count(string, pattern)
            self.assertEqual(result, int(expected))

        with open(Path(__file__).parent.parent / "data" / "v_cholerae_oric.txt", 'r') as stream:
            data = stream.read()

        result = pattern_count(data, "TGATCA")
        expected = 8
        self.assertEqual(result, expected)


class TestLesson_1_3(unittest.TestCase):

    def test_frequency_map(self):


        string = "CGATATATCCATAG"
        length = 3
        result = frequency_map(string, length)
        expected = {'CGA': 1, 'GAT': 1, 'ATA': 3, 'TAT': 2, 'ATC': 1, 'TCC': 1, 'CCA': 1, 'CAT': 1, 'TAG': 1}

        self.assertEqual(result, expected)

    def test_frequent_words(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "FrequentWordsNoDuplicates.txt"
        test_data = common.retrieve_test_data(file_path)
        for (string, count), expected in test_data:
            result = frequent_words(string, int(count))
            expected = expected.split()
            self.assertEqual(result, expected)

        vibrio_cholerae = (
            "CAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTA"
            "CTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGC"
            "GCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTG"
            "ACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTC"
            "AATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATC"
            "ATCGTTTC"
            )
        length = 10
        result = frequent_words(vibrio_cholerae, length)
        expected = ["CTCTTGATCA", "TCTTGATCAT"]

        self.assertEqual(result, expected)

class TestLesson_1_4(unittest.TestCase):

    def test_reverse(self):
        
        pattern = "AAAACCCGGT"
        result = reverse(pattern)
        expected = "TGGCCCAAAA"

        self.assertEqual(result, expected)

    def test_complement(self):

        pattern = "AAAACCCGGT"
        result = complement(pattern)
        expected = "TTTTGGGCCA"

        self.assertEqual(result, expected)

    def test_reverse_complement(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ReverseCompliment.txt"
        test_data = common.retrieve_test_data(file_path)
        for pattern_, expected in test_data:
            pattern = pattern_[0]  # Returns a list by implementation, take the only and first element.
            result = reverse_complement(pattern)
            self.assertEqual(result, expected)

    def test_pattern_matching(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "PatternMatching.txt"
        test_data = common.retrieve_test_data(file_path)
        for (pattern, string), expected_ in test_data:
            expected = [int(item) for item in expected_.split()]
            result = pattern_matching(pattern, string)
            self.assertEqual(result, expected)

        with open(Path(__file__).parent.parent / "data" / "Vibrio_cholerae.txt", 'r') as stream:
            vibrio_cholerae = stream.read()

        pattern = "CTTGATCAT"
        result = pattern_matching(pattern, vibrio_cholerae)
        expected = [60039, 98409, 129189, 152283, 152354, 152411, 163207, 197028, 200160, 357976, 376771, 392723,
                    532935, 600085, 622755, 1065555]
        self.assertEqual(result, expected)

class TestLesson_1_5(unittest.TestCase):

    def test_thermotoga_petrophila(self):
        
        with open(Path(__file__).parent.parent / "data" / "t_petrophila_oriC.txt", 'r') as stream:
            thermotoga_petrophila = stream.read()

        pattern_a = "ATGATCAAG" 
        pattern_b = "CTTGATCAT"
        length = len(pattern_a)

        count_a = frequency_map(thermotoga_petrophila, length).get(pattern_a, 0)
        count_b = frequency_map(thermotoga_petrophila, length).get(pattern_b, 0)

        self.assertEqual(count_a, 0)
        self.assertEqual(count_b, 0)


if __name__ == "__main__":
    unittest.main()

