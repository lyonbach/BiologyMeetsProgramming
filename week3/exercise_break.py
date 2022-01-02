import numpy as np

NUC = list("ACGT")

def e_1_3():
    profile_motifs = np.array(
        [[.2, .2, .0, .0, .0, .0, .9, .1, .1, .1, .3, .0],
        [.1, .6, .0, .0, .0, .0, .0, .4, .1, .2, .4, .6],
        [.0, .0, 1.0, 1.0, .9, .9, .1, .0, .0, .0, .0, .0],
        [.7, .2, .0, .0, .1, .1, .0, .5, .8, .7, .3, .4]]
    )

    logs = np.log2(profile_motifs)
    logs = -np.where(logs!=-np.inf, logs, 0.0)
    entropy = (logs*profile_motifs).sum()
    print(entropy)

def e_1_4():

    consensus = "TCGTGGATTTCC"
    profile_matrix = [
            [0.2, 0.2, 0. , 0. , 0. , 0. , 0.9, 0.1, 0.1, 0.1, 0.3, 0. ],
            [0.1, 0.6, 0. , 0. , 0. , 0. , 0. , 0.4, 0.1, 0.2, 0.4, 0.6],
            [0. , 0. , 0.1, 0.1, 0.9, 0.9, 0.1, 0. , 0. , 0. , 0. , 0. ],
            [0.7, 0.2, 0. , 0. , 0.1, 0.1, 0. , 0.5, 0.8, 0.7, 0.3, 0.4]
        ]

    probability = 1
    for j, char in enumerate(consensus):
        idx = NUC.index(char)
        char_pv = profile_matrix[idx][j]

        print(f"CHAR: {char}")
        print(f"P   : {char_pv}")
        probability *= char_pv
    
    print(probability)
    return probability

e_1_4()