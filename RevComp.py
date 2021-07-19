# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

# Copy your Reverse() function here.
def Reverse(Pattern):
    reverse = ""
    for char in reversed(Pattern):
        reverse += char
    return reverse

# Copy your Complement() function here.
def Complement(Pattern):
    complement = ''
    for base in Pattern:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
    return complement

print(ReverseComplement("TTGTGTC"))