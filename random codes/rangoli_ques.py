# https://github.com/sanskritilakhmani/Hackerrank/blob/main/Python/String/Alphabet_rangoli.py


n = int(input())
data = [chr(97+i) for i in range(n)]
items = list(range(n))
items = items[:-1]+items[::-1]
for i in items:
    temp = data[-(i+1):]
    row = temp[::-1]+temp[1:]
    print("-".join(row).center(n*4-3, "-"))
