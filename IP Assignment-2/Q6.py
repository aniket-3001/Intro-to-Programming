def grade(marks):  # function which returns grade on basis of total marks
    if marks > 80:
        return 'A'
    elif marks <= 80 and marks >= 70:
        return 'A-'
    elif marks < 70 and marks >= 60:
        return 'B'
    elif marks < 60 and marks >= 50:
        return 'B-'
    elif marks < 50 and marks >= 40:
        return 'C'
    elif marks < 40 and marks >= 35:
        return 'C-'
    elif marks < 35 and marks >= 30:
        return 'D'
    else:
        return 'F'


# hardcoded list containing pairs of total marks and weight of the assignment/exam as tuple
wts = [(10, 5), (20, 5), (40, 15), (40, 10), (45, 20), (50, 45)]
marks_l = []  # in this nested list, we will store the marks of each student as a list
roll_l = []  # in this list we store roll no.s of the students

with open("IP Assignment-2/IPmarks.txt") as f:
    for c in f:
        l = (c.strip()).split(', ')
        roll_l += [l[0]]
        marks_l += [[int(c) for c in l[1::]]]

with open("IPgrades.txt", 'w') as f:
    for i in range(len(roll_l)):
        tot_marks = 0
        f.write(f"{roll_l[i]}, ")
        for j in range(len(wts)):
            normalised_marks = (marks_l[i][j]/wts[j][0])*wts[j][1]
            tot_marks += normalised_marks  # calculating total marks
        f.write(f"{tot_marks}, ")
        f.write(f"{grade(tot_marks)}\n")

print("data appended successfully.")
