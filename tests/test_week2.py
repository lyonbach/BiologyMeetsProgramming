from pathlib import Path
import sys
import unittest

PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))

from week2.lesson_1_3 import symbol_array, faster_symbol_array
from week2.lesson_1_4 import skew_array, minium_skew
from week2.lesson_1_5 import approximate_pattern_count, approximate_pattern_matching, hamming_distance

import common


class TestLesson_1_3(unittest.TestCase):
    
    def test_symbol_array(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "SymbolArray.txt"
        test_data = common.retrieve_test_data(file_path)
        for (genome, symbol), expected in test_data:
            result = symbol_array(genome, symbol)
            self.assertEqual(result, expected)

    def test_faster_symbol_array(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "FasterSymbolArray.txt"
        test_data = common.retrieve_test_data(file_path)
        for (genome, symbol), expected in test_data:
            result = faster_symbol_array(genome, symbol)
            self.assertEqual(result, expected)


class TestLesson_1_4(unittest.TestCase):

    def test_short_strand(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "SkewArray.txt"
        test_data = common.retrieve_test_data(file_path)
        for genome_, expected_ in test_data:
            genome = genome_[0]  # By implementation returns list, take the only and first element.
            expected = [int(item) for item in expected_.split()]
            result = skew_array(genome)
            self.assertEqual(result, expected)

    def test_minium_skew(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "MinimumSkew.txt"
        test_data = common.retrieve_test_data(file_path)
        for genome_, expected_ in test_data:
            genome = genome_[0]  # By implementation returns list, take the only and first element.
            expected = [int(item) for item in expected_.split()]
            result = minium_skew(genome)
            self.assertEqual(result, expected)

class TestLesson_1_5(unittest.TestCase):

    def test_hamming_distance(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "HammingDistance.txt"
        test_data = common.retrieve_test_data(file_path)
        for (string_a, string_b), expected in test_data:
            result = hamming_distance(string_a, string_b)
            self.assertEqual(result, int(expected))


    def test_approximate_pattern_matching(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ApproximatePatternMatching.txt"
        test_data = common.retrieve_test_data(file_path)
        for (pattern, string, distance), expected_ in test_data:
            result = approximate_pattern_matching(string, pattern, int(distance))
            expected = [int(item) for item in expected_.split()]
            self.assertEqual(result, expected)

    def test_approximate_pattern_count(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ApproximatePatternCount.txt"
        test_data = common.retrieve_test_data(file_path)
        for (pattern, string, distance), expected in test_data:
            result = approximate_pattern_count(string, pattern, int(distance))
            self.assertEqual(result, int(expected))


if __name__ == "__main__":
    unittest.main()
