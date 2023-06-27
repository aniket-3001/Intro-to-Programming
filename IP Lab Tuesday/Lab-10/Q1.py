class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Classroom:
    def __init__(self, studs):
        self.studs = studs

    def return_max(self):
        max_marks = max([stud.marks for stud in self.studs])
        return [f"{stud.name} {stud.marks}" for stud in self.studs if stud.marks == max_marks]


n = int(input())
studs = []

for _ in range(n):
    name, marks = input().split()
    marks = int(marks)
    studs.append(Student(name, marks))

classroom = Classroom(studs)
for c in classroom.return_max():
    print(c)
