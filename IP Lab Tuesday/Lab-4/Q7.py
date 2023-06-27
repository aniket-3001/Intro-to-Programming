def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_of_digits(n):
    g = n % 10
    n //= 10
    while n > 0:
        g = gcd(g, n % 10)
        n //= 10
    return g


def good_or_bad(n):
    l = len(str(n))
    g = gcd_of_digits(n)
    if n % (l + g) == 0:
        return "good"
    else:
        return "bad"


n = int(input())
print(good_or_bad(n))
