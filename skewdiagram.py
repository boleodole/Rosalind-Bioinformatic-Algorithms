def min_skew(seq: str) -> list:
    """
    Finds the positions of minimum skew values
    :param seq: Provided sequence
    :return: List of indices
    """
    skew_value = 0
    skew_min = 0
    min_value_dict = {skew_min: []}
    # looping all over the sequence
    for i in range(len(seq)):
        # Calculating the skew_value
        if seq[i] == 'G':
            skew_value += 1
        elif seq[i] == 'C':
            skew_value -= 1

        # Changing the key: value pair in the dict
        if skew_value < skew_min:
            # deleting the previous skew_min and its indices
            del min_value_dict[skew_min]
            skew_min = skew_value
            # Updating the dict
            min_value_dict.update({skew_min: [i + 1]})
        elif skew_value == skew_min:
            # adding the index to existing list
            min_value_dict[skew_min].append(i + 1)
    return min_value_dict[skew_min]
f = open('dataset_7_10.txt', 'r')
f = f.read()
skew = min_skew(f)
print(*skew)