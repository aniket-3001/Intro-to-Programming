def pascal(n):
    a = [1]
    print(*a)
    for _ in range(n-1):
        a = [0]+a+[0]
        b = [a[i]+a[i+1] for i in range(len(a)-1)]
        print(*b)
        a = b.copy()
