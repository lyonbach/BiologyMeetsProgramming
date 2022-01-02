
from pathlib import Path
import sys
import unittest

import common

PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))

from week3.lesson_1_3 import score
from week4.lesson_1_1 import count_with_pseudo_codes, profile_with_pseudo_codes, greedy_motif_search_with_pseudo_counts
from week4.lesson_1_2 import motifs
from week4.lesson_1_4 import normalize


class TestLesson_1_1(unittest.TestCase):

    def test_count_with_pseudo_codes(self):
        
        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "CountWithPseudocounts.txt"
        test_data = common.retrieve_test_data(str(file_path))
        for motifs, expected in test_data:
            result = count_with_pseudo_codes(motifs)
            self.assertEqual(result, expected)

    def test_profile_with_pseudo_codes(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ProfileWithPseudocounts.txt"
        test_data = common.retrieve_test_data(str(file_path))
        for motifs, expected in test_data:
            result = profile_with_pseudo_codes(motifs)
            self.assertEqual(result, expected)

    def test_greedy_motif_search_with_pseudo_codes(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "GreedyMotifSearchWithPseudocounts.txt"
        test_data = common.retrieve_test_data(str(file_path), output_as_list=True)
        for item, expected in test_data:
            k_t = item.pop(0)
            k, t = [int(_) for _ in k_t.split()]
            result = greedy_motif_search_with_pseudo_counts(item, k, t)
            self.assertEqual(result, expected)

    def test_greedy_motif_search_with_pseudo_codes_on_dosr(self):

        file_path = PROJECT_DIRECTORY / "data" / "DosR.txt"
        k = 15  # k-mer length = 15
        t = 10  # 
        with open(str(file_path), 'r') as stream:
            dna = [_.rstrip() for _ in stream.readlines()]

        result = greedy_motif_search_with_pseudo_counts(dna, k, t)
        expected = ["GGACTTCAGGCCCTA",
                    "GGTCAAACGACCCTA",
                    "GGACGTAAGTCCCTA",
                    "GGATTACCGACCGCA",
                    "GGCCGAACGACCCTA",
                    "GGACCTTCGGCCCCA",
                    "GGACTTCTGTCCCTA",
                    "GGACTTTCGGCCCTG",
                    "GGACTAACGGCCCTC",
                    "GGACCGAAGTCCCCG"]
        expected_motifs_score = 35
        self.assertEqual(result, expected)
        self.assertEqual(score(result), expected_motifs_score)

class TestLesson_1_2(unittest.TestCase):

    def test_motifs(self):

        def get_profile_matrix(rows):

            return dict(zip("ACGT", [[float(item) for item in row.split()] for row in rows]))
                

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "MotifsProfileDna.txt"
        test_data = common.retrieve_test_data(str(file_path), output_as_list=True)
        k = 4
        for inputs, expected in test_data:
            profile_matrix = get_profile_matrix(inputs[:4])
            dna = inputs[4:]
            result = motifs(profile_matrix, k, dna)
            self.assertEqual(result, expected)

    def test_normalize(self):

        test_data = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
        result = normalize(test_data)
        expected = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()