# Takes a sequence Pattern (k-mer) and finds its frequency with at most d mismatches
def app_pattern_match(Pattern, Genome, d):
    positions = 0
    for i in range(len(Genome) - len(Pattern) + 1):
        Pattern_2 = Genome[i:i + len(Pattern)]
        if hamming_distance(Pattern, Pattern_2) <= d:
            positions = positions + 1

    return positions

# This function matches 2 strings of the same length and searches for mismatches.
# If there are more mismatches than imposed, then the string is filtered.
def hamming_distance(string_1, string_2):
    count = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            count += 1
    return count


print(app_pattern_match('CTGTAT','CCTGTGGTACCTCCCGGCCTCCCAAAGAAATCGCAGATCATTGCCTACTGAGCGCCGCTATACGCTCTGCGGCAGACCGGAACTGCTTATGTGGTACGACCGAGATTGAGAGATAGGGTCTGTATTGGATCTCTACCCACCGTTTGCTCACCATAACTTTACATTGACCTAGGCTATTAAGCAACATTTACCAAATTCTGTCTCATCCGGTTATGGCAACTCTACAGGATTATGAGTCTCGAGGAATCTCACACAAATGAGATTGAATGATCGTCCGTTGGACTACCGCTCGTGACCATAGTGCACCTTGTCGATGCATAGGGTGGTCAGAGCGCCCTATAGCCGCAGTTTCACTTGATATATACCGAGCAGGAGCCCCCTATGCGATAGCCGATTC', 2))