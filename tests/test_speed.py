from pathlib import Path
import random
import sys
import time


PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))
from week3.lesson_1_3 import consensus, count, np_consensus, np_count

NUC = list("ACGT")

test_data_3 = (
    (["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"], "CACCTA"),
    (["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA",
        "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"], "GACTAAGGGT")
)

length = 5000
motifs = [random.choices(NUC, k=length) for i in range(100)]


def test_consensus():

    k = 100
    ti = time.time()
    for _ in range(k):
        consensus(motifs)
    print(f"Ran \"consensus\" in {time.time() - ti} seconds")

    ti = time.time()
    for _ in range(k):
        np_consensus(motifs)
    print(f"Ran \"np_consensus\" in {time.time() - ti} seconds")

def test_count():

    k = 100
    ti = time.time()
    for _ in range(k):
        count(motifs)
    print(f"Ran \"count\" in {time.time() - ti} seconds")

    ti = time.time()
    for _ in range(k):
        np_count(motifs)
    print(f"Ran \"np_count\" in {time.time() - ti} seconds")

test_consensus()
# test_count()