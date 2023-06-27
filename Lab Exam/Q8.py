class Student:
    def __init__(self, rollno, name):
        self.roll = rollno
        self.name = name
        self.courses = {}
        self.avg = 0

    def add_course(self, cno, grade):
        self.courses[cno] = grade

    def avg_grade(self):
        self.avg = sum(list(self.courses.values())) / \
            len(list(self.courses.values()))

    def stud_rec(self):
        print(f"name: {self.name}")
        print(f"roll no.: {self.roll}")
        print(f"list of courses: {list(self.courses.keys())}")
        print(f"average grade: {self.avg}")


s = Student("stu1", "23001")
s.add_course("cs101", 9)
s.add_course("M101", 8)
s.avg_grade()
s.stud_rec()
