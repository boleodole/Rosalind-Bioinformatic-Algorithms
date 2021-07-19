string = "ABCDGEF"

# Returns a reversed string
def reversing(string):
    reverse_string = ""
    for char in reversed(string):
        reverse_string += char
    return reverse_string

print(reversing(string))