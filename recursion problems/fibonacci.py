def fibonacci(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


n = int(input("Enter how many terms of the Fibonacci series you want to get printed: "))

fib_series = [fibonacci(i) for i in range(n)]
print(*fib_series)
