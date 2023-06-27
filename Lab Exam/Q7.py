lst = [1, 1, 2, 2, 1, 3, 2, 4, 5, 2, 6, 7, 8, 9]
elt = 2
freq_dict = {}
index = 0
for c in lst:
    if c in freq_dict:
        freq_dict[c].append(index)
    else:
        freq_dict[c] = [index]
    index += 1

for c in freq_dict:
    if c == elt:
        print(f"frequency: {len(freq_dict[c])}")
        print(f"indices: {(freq_dict[c])}")
