import copy
from pathlib import Path
import sys

PROJECT_PATH = Path(__file__).parent.parent
sys.path.append(str(PROJECT_PATH))
from week4.lesson_1_4 import gibbs_sampler
from week3.lesson_1_3 import consensus, score


def e_1_4():

    with open(str(PROJECT_PATH / "data" / "DosR.txt"), 'r') as stream:
        dosR = [line.rstrip() for line in stream.readlines()]

    best_motifs = []
    k_mer_length, motif_count, iteration_count = 20, len(dosR), 1000
    for _ in range(20):
        motifs = gibbs_sampler(dosR, k_mer_length, motif_count, iteration_count)
        if not best_motifs:
            best_motifs = copy.copy(motifs)
            continue
        if score(motifs) < score(best_motifs):
            best_motifs = copy.copy(motifs)

    print(best_motifs)
    print(score(best_motifs))
    print(consensus(best_motifs))

e_1_4()
