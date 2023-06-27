# solve q1 without using DictReader and DictWriter

import csv

with open("IP TUTS/TUT-8/Extra/data.csv") as f1:
    csv_r = csv.reader(f1)
    header = next(csv_r)
    header.append("average")
    with open("IP TUTS/TUT-8/Extra/new_data.csv", 'w', newline='') as f2:
        csv_w = csv.writer(f2)
        csv_w.writerow(header)
        for line in csv_r:
            line.append(str(sum([float(c) for c in line[1:]])/len(line[1:])))
            csv_w.writerow(line)
        print("Written to file successfully.")
