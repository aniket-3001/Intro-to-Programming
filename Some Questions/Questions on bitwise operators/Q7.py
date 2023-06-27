n1 = int(input("enter first no.: "))
n2 = int(input("enter second no.: "))
cnt = 0
if n1 > n2:
    while n1 > 0:
        if (n1 & 1) != (n2 & 1):
            cnt += 1
        n1, n2 = n1 >> 2, n2 >> 2
else:
    while n2 > 0:
        if (n1 & 1) != (n2 & 1):
            cnt += 1
        n1, n2 = n1 >> 2, n2 >> 2
if cnt == 1:
    print("True")
else:
    print("False")
