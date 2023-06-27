import time


def assign_grade(studs, policy):  # function to set the grade for each student
    for rollno, marks_and_tot_marks in studs.items():
        tot_marks = marks_and_tot_marks[1]
        if tot_marks >= policy[0]:
            grade = 'A'
        elif tot_marks >= policy[1]:
            grade = 'B'
        elif tot_marks >= policy[2]:
            grade = 'C'
        elif tot_marks >= policy[3]:
            grade = 'D'
        else:
            grade = 'F'
        studs[rollno].append(grade)
    return studs


def generate_summary(course, studs):
    print("Course name:", course["cname"])
    print()

    print("Course credits:", course["credits"])
    print()

    print("Assessments: ")
    for assessment in course["assessments"]:
        print(f"assessment: {assessment[0]}, weight: {assessment[1]}")
    print()

    print("Grading policy:")
    print(f"A: >= {course['policy'][0]}")
    print(f"B: >= {course['policy'][1]}")
    print(f"C: >= {course['policy'][2]}")
    print(f"D: >= {course['policy'][3]}")
    print(f"F: < {course['policy'][3]}")
    print()

    print("Grading Summary: ")
    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    print()
    for rollno in studs:
        grades[studs[rollno][2]] += 1
    for grade in grades:
        print(f"{grade}: {grades[grade]}")


def search_stud(rollno, studs, course):
    if rollno in studs:
        marks_and_tot_marks = studs[rollno]
        marks = marks_and_tot_marks[0]
        assessments = course["assessments"]
        for i, assessment in enumerate(assessments):
            assessment_name, max_marks = assessment
            print(f"{assessment_name} marks: {marks[i]}/{max_marks}")
        tot_marks = marks_and_tot_marks[1]
        print(f"Total marks: {tot_marks}")
        grade = marks_and_tot_marks[2]
        print(f"Grade: {grade}")
    else:
        print(f"Student with roll number {rollno} not found.")


def get_cutoffs(studs):  # function to get updated policy

    def return_marks_list(studs):
        stud_marks = []
        for stud in studs.values():
            stud_marks.append(stud[1])
        return stud_marks

    def relative_mark(lst):
        if len(lst) == 1:
            return lst[0]
        lst = sorted(lst)
        max_diff = 0
        max_index = 0
        for i in range(len(lst)-1):
            diff = lst[i+1] - lst[i]
            if diff > max_diff:
                max_diff = diff
                max_index = i
        return (lst[max_index]+lst[max_index+1])/2

    updated_cutoffs = []
    grade_dict = {'A': [], 'B': [], 'C': [], 'D': []}
    marks = return_marks_list(studs)

    for c in marks:
        if c >= 38 and c <= 42:
            grade_dict['D'].append(c)
        elif c >= 48 and c <= 52:
            grade_dict['C'].append(c)
        elif c >= 63 and c <= 67:
            grade_dict['B'].append(c)
        elif c >= 78 and c <= 82:
            grade_dict['A'].append(c)

    for c in enumerate(list(grade_dict.values())):
        if c[1] == []:
            if c[0] == 0:
                updated_cutoffs.append(80)
            elif c[0] == 1:
                updated_cutoffs.append(65)
            elif c[0] == 2:
                updated_cutoffs.append(50)
            elif c[0] == 3:
                updated_cutoffs.append(40)
        else:
            updated_cutoffs.append(relative_mark(c[1]))

    return updated_cutoffs  # returns the cutoff list


def write_grades_to_file(fname, studs):
    with open(fname, 'w') as f:
        for stud in studs:
            f.write(f"{stud}, {studs[stud][1]}, {studs[stud][2]}\n")
    print("Printed in file successfully.")


studs = {}
with open("IP Assignment-3/students_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(', ')
        # since last element is roll no.
        marks = [float(mark) for mark in data[:-1]]
        rollno = data[-1]
        studs[rollno] = [marks, sum(marks)]

studs = dict(sorted(studs.items(), key=lambda item: item[1][1]))

c1 = {"cname": "IP", "credits": 4, "assessments": [
    ("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)], "policy": [80, 65, 50, 40]}

c1["policy"] = get_cutoffs(studs)

studs = assign_grade(studs, c1["policy"])

# # Set the menu
# print("Menu:")
# print("1. Print summary")
# print("2. Print the grades of all the students in a file as: rollno, total marks, grade")
# print("3. Get student record")
# print("Hit enter without providing any input to terminate the program\n")
# while True:
#     ch = input("Enter choice: ")
#     if ch == '1':
#         generate_summary(c1, studs)
#     elif ch == '2':
#         write_grades_to_file("IP Assignment-3/students_output.txt", studs)
#     elif ch == '3':
#         rollno = input("enter roll no. to be searched: ")
#         search_stud(rollno, studs, c1)
#     elif ch == ' ':
#         break
#     else:
#         print("Invalid choice. Please try again.")

# for writing grades to file
st_time1 = time.time()
for n in range(1000):
    write_grades_to_file("IP Assignment-3/students_output.txt", studs)
ed_time1 = time.time()

# for searching for student
st_time2 = time.time()
for n in range(1000):
    search_stud(rollno, studs, c1)
ed_time2 = time.time()

print("time taken for grading in dictionary approach:", ed_time1-st_time1)
print("time taken for searching student in dictionary approach:", ed_time2-st_time2)
