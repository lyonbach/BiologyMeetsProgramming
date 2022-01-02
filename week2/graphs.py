from pathlib import Path
import sys

from matplotlib import pyplot as plt

PROJECT_DIRECTORY = Path(__file__).parent.parent
sys.path.append(str(PROJECT_DIRECTORY))

import week2.lesson_1_3 as lesson_1_3
import week2.lesson_1_4 as lesson_1_4
import week2.lesson_1_5 as lesson_1_5


FONT_SIZE = 12

def get_genome_data(file_name):

    with open(str(PROJECT_DIRECTORY/ "data" / file_name), 'r')  as stream:
        data = stream.read()

    if not data:
        raise IOError("Put the E_coli.txt under <project folder> / data")

    return data

def draw_nucleotide_count_graph(genome_data, adjust_x_scale=False):


    symbols = ['C', 'A', 'T', 'G']

    # Adjustments and styling
    plt.style.use('seaborn-whitegrid')
    # plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = str(FONT_SIZE)

    # Plot
    for symbol in symbols:
        mapping = lesson_1_3.faster_symbol_array(genome_data, symbol)
        plt.plot(mapping.keys(), mapping.values())

    if adjust_x_scale:
        plt.xticks(range(0, max(mapping.keys()), int(25e4)))

    # Labels and Legend
    plt.xlabel("Offset (*how many nucleotides the window has been moved)")
    plt.ylabel(f"Occurrance of Nucleotide")
    plt.legend(symbols)
    plt.show()

def draw_skew_diagram(genome_data, title):

    s_array = lesson_1_4.skew_array(genome_data)

    # Adjustments and styling
    plt.style.use('seaborn-whitegrid')
    # plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = str(FONT_SIZE)
    plt.title(title)

    # Plot
    plt.plot(range(len(s_array)), s_array)

    # Labels and Legend
    plt.xlabel("Position")
    plt.ylabel("Skew")
    plt.show()

    #TODO: CREATE A FUNCTION, SHOW ORI AND TER ON GRAPH

if __name__ == "__main__":

    draw_nucleotide_count_graph("GATACACTTCCCGAGTAGGTACTG")
    draw_skew_diagram("GATACACTTCCCGAGTAGGTACTG", "Skew Diagram of Arbitrary String:\nGATACACTTCCCGAGTAGGTACTG")
    
    # E. Coli
    genome_data = get_genome_data("E_coli.txt")
    draw_nucleotide_count_graph(genome_data, adjust_x_scale=True)
    draw_skew_diagram(genome_data, "Skew Diagram: E. Coli")
