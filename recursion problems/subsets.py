def f(lst, i=0, set=set()):
    global subsets
    if i == len(lst):
        subsets.append(set.copy())
        return
    f(lst, i+1, set.copy())
    set.add(lst[i])
    f(lst, i+1, set.copy())


subsets = []


l = list(map(int, input().split()))
f(l)
print(subsets)
