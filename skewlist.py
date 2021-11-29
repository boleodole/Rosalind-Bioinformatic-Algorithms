def min_skew(seq: str) -> list:
    """
    List of Skew values, and minimum skew value
    """
    skew_value = 0
    min_list = [0]
    # looping all over the sequence
    for i in range(len(seq)):
        # Calculating the skew_value
        if seq[i] == 'G':
            skew_value += 1
        elif seq[i] == 'C':
            skew_value -= 1
        min_list.append(skew_value)
    skew_min = min(min_list)
    return min_list
print(*min_skew('GAGCCACCGCGATA'))
