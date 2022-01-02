from pathlib import Path
import sys
import unittest
import common


PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))

from week3.lesson_1_3 import consensus, count, np_consensus, np_count, np_profile, profile, score
from week3.lesson_1_4 import greedy_motif_search, pr, profile, profile_most_probable_pattern


class TestLesson_1_3(unittest.TestCase):

    def test_count(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "CountMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = count(motifs)
            self.assertEqual(result, expected)

    def test_np_count(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "CountMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = np_count(motifs)
            self.assertEqual(result, expected)

    def test_profile(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ProfileMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = profile(motifs)
            self.assertEqual(result, expected)

    def test_np_profile(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ProfileMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = np_profile(motifs)
            self.assertEqual(result, expected)

    def test_consensus(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ConsensusMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = consensus(motifs)
            self.assertEqual(result, expected)

    def test_np_consensus(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ConsensusMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = np_consensus(motifs)
            self.assertEqual(result, expected)

    def test_score(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "ScoreMotifs.txt"
        test_data = common.retrieve_test_data(file_path)
        for motifs, expected in test_data:
            result = score(motifs)
            self.assertEqual(result, int(expected))


class TestLesson_1_4(unittest.TestCase):

    def build_matrix(self, rows):
        return dict(zip("ACGT", [[float(item) for item in row.split()] for row in rows]))

    def test_pr(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "Pr.txt"
        test_data = common.retrieve_test_data(file_path)
        for inputs, expected in test_data:
            string = inputs.pop(0)
            profile_ = self.build_matrix(inputs)
            result = pr(string, profile_)
            self.assertAlmostEqual(result, float(expected), delta=10e-15)

    def test_profile_most_probable_pattern(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "Profile-mostProbableKmer.txt"
        test_data = common.retrieve_test_data(file_path)
        for inputs, expected in test_data:
            string = inputs.pop(0)
            length = int(inputs.pop(0))
            profile_ = self.build_matrix(inputs)
            result = profile_most_probable_pattern(string, length, profile_)
            self.assertEqual(result, expected)

    def test_greedy_motif_search(self):

        file_path = PROJECT_DIRECTORY / "data" / "test_data" / "GreedyMotifSearch.txt"
        test_data = common.retrieve_test_data(file_path, output_as_list=True)
        for inputs, expected in test_data:
            k, t = [int(item) for item in inputs.pop(0).split()]
            result = greedy_motif_search(inputs, k, t)
            self.assertEqual(result, expected)

        with open(Path(__file__).parent.parent / "data" / "DosR.txt") as stream:
            dosr_data = [line.replace('\n', '') for line in stream.readlines()]

        expected = ["GTTAGGGCCGGAAGT",
                    "CCGATCGGCATCACT",
                    "ACCGTCGATGTGCCC",
                    "GGGTCAGGTATATTT",
                    "GTGACCGACGTCCCC",
                    "CTGTTCGCCGGCAGC",
                    "CTGTTCGATATCACC",
                    "GTACATGTCCAGAGC",
                    "GCGATAGGTGAGATT",
                    "CTCATCGCTGTCATC"]

        result = greedy_motif_search(dosr_data, 15, len(dosr_data))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
