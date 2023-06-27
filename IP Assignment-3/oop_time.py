import time


class Student:
    def __init__(self, rollno, marks):
        self.rollno = rollno
        self.marks = marks
        self.tot_marks = sum(marks)
        self.grade = ''

    def get_grade(self, policy):
        if self.tot_marks >= policy[0]:
            self.grade = 'A'
        elif self.tot_marks >= policy[1]:
            self.grade = 'B'
        elif self.tot_marks >= policy[2]:
            self.grade = 'C'
        elif self.tot_marks >= policy[3]:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def search_stud(self, rollno):
        if stud.rollno == rollno:
            print("Marks: ")
            for i in range(len(assessments)):
                print(f"{assessments[i][0]}: {stud.marks[i]}")
            print()
            print("Total marks:", stud.tot_marks)
            print()
            print("Grade:", stud.grade)
            return 1


class Course:
    def __init__(self, cname, credits, assessments, policy, studs):
        self.cname = cname
        self.credits = credits
        self.assessments = assessments
        self.studs = studs
        self.policy = self.get_cutoffs()

    # method which returns the cutoff list on basis of performance of students
    def get_cutoffs(self):

        def return_marks_list(studs):
            stud_marks = []
            for stud in studs:
                stud_marks.append(stud.tot_marks)
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
        marks = return_marks_list(self.studs)

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

    def generate_summary(self):
        print("Course name:", self.cname)
        print()

        print("Course credits:", self.credits)
        print()

        print("Assessments: ")
        for assessment in self.assessments:
            print(f"assessment: {assessment[0]}, weight: {assessment[1]}")
        print()

        print("Grading policy:")
        print(f"A: >= {self.policy[0]}")
        print(f"B: >= {self.policy[1]}")
        print(f"C: >= {self.policy[2]}")
        print(f"D: >= {self.policy[3]}")
        print(f"F: < {self.policy[3]}")
        print()

        print("Grading Summary: ")
        grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        print()
        for stud in self.studs:
            stud.get_grade(self.policy)
            grades[stud.grade] += 1
        for grade in grades:
            print(f"{grade}: {grades[grade]}")


cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15),
               ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40]

studs = []
with open("IP Assignment-3/students_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(', ')
        marks = [float(mark) for mark in data[:-1]]
        rollno = data[-1]  # since last element is roll no.
        studs.append(Student(rollno, marks))

studs.sort(key=lambda x: x.tot_marks, reverse=True)

IP = Course(cname, credits, assessments, policy,
            studs)  # object of Course class


def write_grades_to_file(fname):
    with open(fname, 'w') as f:
        for stud in IP.studs:
            stud.get_grade(IP.policy)
            f.write(f"{stud.rollno}, {stud.tot_marks}, {stud.grade}\n")
    print("Printed in file successfully.")


# # set the menu
# print("menu:")
# print("1. Generate summary")
# print("2. Generate grades for all students")
# print("3. Get student record")
# print("Exit by pressing enter key without giving any input\n")


# while True:
#     ch = input("enter choice: ")
#     print()

#     if ch == '1':
#         IP.generate_summary()
#         print()

#     elif ch == '2':
#         write_grades_to_file("IP Assignment-3/students_output.txt")
#         print()

#     elif ch == '3':
#         s_rollno = input("enter roll no. to be searched: ")
#         found = 0
#         for stud in studs:
#             stud.get_grade(IP.policy)
#             if stud.search_stud(s_rollno):
#                 found = 1
#                 break
#         if not found:
#             print(f"No student found with roll no.: {s_rollno}")
#         print()

#     elif ch == '':
#         break

#     else:
#         print("Invalid choice. Please try again.")

st_time1 = time.time()
for n in range(1000):
    write_grades_to_file("IP Assignment-3/students_output.txt")
ed_time1 = time.time()

st_time2 = time.time()
for n in range(1000):
    for stud in studs:
        stud.get_grade(IP.policy)
        if stud.search_stud("2022005"):
            break
ed_time2 = time.time()

print("time taken for grading in OOP approach:", ed_time1-st_time1)
print("time taken for searching student in OOP approach:", ed_time2-st_time2)
