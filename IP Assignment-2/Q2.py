def valid_course_no(course_no):  # function to check for valid course no.
    for c in course_no:
        if not c.isalnum():
            print("improper course no")
            print()
            return False
    if not course_no[:2:].isupper():
        print("improper course no")
        print()
        return False
    if not course_no[-2].isdigit():
        print("improper course no")
        print()
        return False
    return True


def valid_no_credits(cred):  # function to check for valid credit
    if cred not in ['1', '2', '4']:
        print("incorrect credit")
        print()
        return False
    return True


def valid_grad(grad):  # function to check for valid grade
    if grad not in ['A+', 'A', 'A-', 'B', 'B-', 'C', 'C-', 'D', 'F']:
        print("incorrect grade")
        print()
        return False
    return True


def return_course_list(course_no, cred, grad):
    course = []
    if valid_course_no(course_no) and valid_no_credits(cred) and valid_grad(grad):
        course += [course_no, cred, grad]
        if grad == 'A' or grad == 'A+':
            course += [10]
        elif grad == 'A-':
            course += [9]
        elif grad == 'B':
            course += [8]
        elif grad == 'B-':
            course += [7]
        elif grad == 'C':
            course += [6]
        elif grad == 'C-':
            course += [5]
        elif grad == 'D':
            course += [4]
        else:
            course += [2]
        return course
    else:
        return False


def sgpa(l):
    tot_cred = 0
    cred_grad = 0
    for c in l:
        cred_grad += int(c[1])*int(c[3])
        tot_cred += int(c[1])
    sgpa = cred_grad/tot_cred
    return sgpa


l = []
while True:
    s = input("enter space separated details for student (eg. CSE101 4 A): ")
    if s == "":
        break
    s = s.split()
    course = return_course_list(s[0], s[1], s[2])
    if course != False:
        l += [tuple(course)]

l = sorted(l, key=lambda x: x[0])

print()
for c in l:
    print(f"{c[0]}: {c[2]}")

print()

print("SGPA:", round(sgpa(l), 2))
