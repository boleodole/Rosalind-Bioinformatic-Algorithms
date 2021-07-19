def skew_diagram(Genome):
    skew = [0]
    status = 0
    n = len(Genome)
    for i in range(n):
        for nucleotide in Genome[i]:
            if nucleotide == 'A':
                status = status + 0
                skew.append(status)
            elif nucleotide == 'T':
                status = status + 0
                skew.append(status)
            elif nucleotide == 'C':
                status = status - 1
                skew.append(status)
            elif nucleotide == 'G':
                status = status + 1
                skew.append(status)
    minpos = minimum_position(skew)
    return minpos

def minimum_position(list):
    min_value = min(list)
    if list.count(min_value) > 1:
        return [i for i, x in enumerate(list) if x == min(list)]
    else:
        return skew.index(min(1))

f = open('dataset_7_10.txt', 'r')
f = f.read()
print(skew_diagram(f))