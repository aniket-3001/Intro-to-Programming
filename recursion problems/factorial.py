def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)


num = int(input("enter number whose factorial you require: "))

print(fact(num))
