import math


def prime_factors(num):
    while num % 2 == 0:
        print(2, end=' ')
        num = num/2
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            print(int(i), end=' ')
            num = num/i
    if num > 2:
        print(int(num))


num = int(input())
prime_factors(num)
