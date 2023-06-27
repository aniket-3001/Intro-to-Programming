dict = {}
with open("marks.txt") as f:
    for line in f:
        data = ((line.strip()).split())
        marks = [int(c) for c in data[1:]]
        if sum(marks)/5 >= 80:
            dict[data[0]] = marks

with open("toppers.txt", 'w') as f:
    for key in dict:
        s = f"{key} {' '.join(str(c) for c in dict[key])}\n"
        f.write(s)
    print("written in file successfully")
