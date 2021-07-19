Pattern = "CGC"
Genome = "ATGACTTCGCTGTTACGCGC"

Position = []
for i in range(len(Genome) - len(Pattern)+1):
    if Genome[i:i + len(Pattern)] == Pattern:
        Position.append(i)
print(*Position)