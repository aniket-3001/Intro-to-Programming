# WAP to count the number of ways of partitioning n objects using parts upto m. Take m and n as input from user.

def partition(m, n):
    if m == 0 or n < 0:
        return 0
    if n == 0:
        return 1
    return partition(m, n-m)+partition(m-1, n)


m, n = map(int, input(" enter space separated values for m and n: ").split())
print("number of ways of partitioning:", partition(m, n))
