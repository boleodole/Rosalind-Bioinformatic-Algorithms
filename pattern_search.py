# Copy your PatternCount function from the previous step below this line
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"

Text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"

Pattern = "CGCG"

count = PatternCount(Text, Pattern)
print(count)


# Finally, print the result of calling PatternCount on Text and Pattern.
# Don't forget to use the notation print() with parentheses included!