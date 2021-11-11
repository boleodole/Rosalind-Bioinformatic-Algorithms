def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


Text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"

Pattern = "CGCG"

count = PatternCount(Text, Pattern)
print(count)
