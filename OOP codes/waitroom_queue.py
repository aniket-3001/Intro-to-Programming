class Queue:
    def __init__(self):
        self.qdata = []
        self.front = 0
        self.end = 0

    def add(self, obj):
        self.qdata.append(obj)
        self.end += 1

    def remove(self):
        if self.isempty():
            return None
        obj = self.qdata[self.front]
        self.front += 1
        self.end -= 1
        return obj

    def isempty(self):
        return self.front == len(self.qdata)


print("1: add, 2: remove, -1: exit:\n")


def studentq():
    waitroom = Queue()
    while True:
        op = int(input("enter operation: "))
        if op == 1:
            rollno = input("Give roll no: ")
            waitroom.add(rollno)
        elif op == 2:
            obj = waitroom.remove()
            if obj == None:
                print("No student waiting")
            else:
                print(f'Next student: {obj}')
        elif op == -1:
            break
        else:
            print("Incorrect command, try again")
        print()
    print("office Hr ended")
    print(f"no. of students waiting: {waitroom.end}")


studentq()
