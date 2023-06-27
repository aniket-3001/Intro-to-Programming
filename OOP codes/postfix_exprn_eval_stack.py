# code for postfix
# (a+b)*c => ab+c*
# a/b+c/d => ab/cd/+
# (a+b)*(c+d) => ab+cd+*

class Stack:
    def __init__(self):
        self.top = 0
        self.data = []

    def push(self, item):
        self.data.append(item)
        self.top += 1

    def pop(self):
        if self.isempty():
            print("Error - popping empty stack")
            return
        self.top -= 1
        return self.data.pop()

    def isempty(self):
        return self.top <= 0


def postfix(l):
    estk = Stack()
    for i in l:
        if isinstance(i, (float, int)):
            estk.push(i)
        elif isinstance(i, str):
            if i in ('+', '-', '*', '/'):
                if estk.isempty():
                    return "Error - Not enough operands"
                y = estk.pop()
                if estk.isempty():
                    return "Error - Not enough operands"
                x = estk.pop()
                if i == '+':
                    estk.push(x+y)
                elif i == '-':
                    estk.push(x-y)
                elif i == '*':
                    estk.push(x*y)
                elif i == '/':
                    estk.push(x/y)
            else:
                return "Error - Invalid operator"
    if estk.isempty():
        return "Error - Not enough operands"
    if estk.top > 1:
        return "Error - Not enough operators"
    return estk.pop()


lst = list(map(int, input().split()))
print(postfix(lst))
