def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


a = int(input())
b = int(input())
print(gcd(a, b))
