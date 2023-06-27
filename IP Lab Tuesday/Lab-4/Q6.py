import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n = int(input())
if n % 2 == 0:
    for i in range(2, n):
        if is_prime(i):
            j = n - i
            if is_prime(j):
                print(i, j)
                break
