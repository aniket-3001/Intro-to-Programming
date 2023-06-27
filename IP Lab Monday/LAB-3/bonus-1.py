# https://www.hackerrank.com/contests/lab-3-monday/challenges/lab-3q5-sequence-function

def left_right_sum(l, index):
    if index == 0:
        print(0, sum(l)-l[0])
    elif index == len(l)-1:
        print(sum(l)-l[len(l)-1], 0)
    else:
        print(sum(l[index-1::-1]), sum(l[index+1::]))


l = list(map(int, input().split()))
for i in range(len(l)):
    min_ele_index = l.index(min(l))
    max_ele_index = l.index(max(l))
    left_right_sum(l, min_ele_index)
    l[min_ele_index] = l[max_ele_index]+1
