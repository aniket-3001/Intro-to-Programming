# https://www.hackerrank.com/contests/lab-4-monday/challenges/lab-4q6-grading-series/submissions/code/1353269885

def desired_strings(l):
    if len(l) % 2 == 0:
        str1 = ''
        str2 = ''
        for _ in range(len(l)//2):
            str1 += 'BA'
            str2 += 'AB'
    else:
        str1 = 'A'
        str2 = 'B'
        for i in range(len(l)//2):
            str1 += 'BA'
            str2 += 'AB'
    return [str1, str2]


def divisor(l, string_list):
    if len(l) == 1:
        return 1
    else:
        for i in range(2, max(l)+1):
            str = ""
            for c in l:
                if c % i == 0:
                    str += "A"
                else:
                    str += "B"
            if str in string_list:
                return i
        return -1


l = list(map(int, input().split()))
print(divisor(l, desired_strings(l)))
