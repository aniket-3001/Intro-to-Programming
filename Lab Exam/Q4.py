def tuple_lst():
    global lst, gr, sm, n
    if n == len(sm):  # once the length of smaller list is covered, instead of printing tuples just print the remaining elements of the greater list
        print(lst+gr[n:])
        return
    lst.append((gr[n], sm[n]))
    n += 1
    return tuple_lst()


n = 0
l1 = list(map(str, input().split()))
l2 = list(map(str, input().split()))

if len(l1) > len(l2):
    gr = l1
    sm = l2
else:
    sm = l1
    gr = l2

lst = []

tuple_lst()
