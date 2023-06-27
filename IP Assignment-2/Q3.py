# function accepting file object as a parameter and returns its elements in the form of a dictionary
def create_yrbook_dict(f):
    dict = {}

    for line in f:
        if line.strip() == '':
            dict[stud_name] = d
            continue
        elif ':' in line:
            d = {}
            stud_name = line.strip(':\n')
        else:
            l = (line.strip()).split(', ')
            d[l[0]] = int(l[1])

    return dict


with open("IP Assignment-2/stud.txt") as f_stud:
    # storing elements of file "stud.txt" in the form of a dictionary using this function call
    yearbook = create_yrbook_dict(f_stud)

max = 0
min = 1e5
L_max = []
L_min = []

for c in yearbook.values():  # determining the max and min no. of signatures
    cnt = list(c.values()).count(1)
    if cnt > max:
        max = cnt
    if cnt < min:
        min = cnt

for c in yearbook:  # storing the name of the students with max and min no. of signatures
    if list(yearbook[c].values()).count(1) == max:
        L_max += [c]
    if list(yearbook[c].values()).count(1) == min:
        L_min += [c]

# displaying students with max no. of signatures
print("Students with the maximum no. of signatures are: ", end='')
print(', '.join(L_max))

print()

# displaying students with min no. of signatures
print("Students with the minimum no. of signatures are: ", end='')
print(', '.join(L_min))
