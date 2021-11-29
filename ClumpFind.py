# Slides a window of length L trough the genome to find frequent k-mers and then checks if some of the k-mers
# appear more or equal than t times
def FindClumps(Text, k, L, t):
    Patterns = [] # This list stores k-mers that appear more than t times
    n = len(Text)
    for i in range(n-k+1):
        Window = Text[i:i+L]
        freqMap = FrequencyMap(Window, k)
        for s in freqMap:
            if freqMap[s] >= t:
                if s not in Patterns:
                    Patterns.append(s)
    return Patterns

#This function maps the frequent k-mers and lists how many times they appear in a given genome (string)
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq
f = open('dataset_7_10.txt', 'r')
f = f.read()
print(FindClumps(f, 9, 20, 2)) # The result shows that there are 5 9-mers that appear 2 times in the given DNA seq.
