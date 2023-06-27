class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def Set(self, name, age):
        self.name = name
        self.age = age

    def GetBioData(self):
        return f"Name, Age and Gender of student is {self.name}, {self.age} and {self.gender}"


lst = []
n = int(input())
for _ in range(3*n):
    s = input()
    lst += [s]

studs = []
for i in range(n):
    name = lst[3*i]
    age = lst[(3*i)+1]
    gender = lst[(3*i)+2]
    stud = Student(name, age, gender)
    studs.append(stud)

for stud in studs:
    stud.Set(stud.name, stud.age)
    print(stud.GetBioData())
