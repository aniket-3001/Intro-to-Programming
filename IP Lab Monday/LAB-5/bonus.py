# https://www.hackerrank.com/contests/lab-5-monday/challenges/lab-4bonus-axis

def revisits(lst):
    var = lst[0]
    cnt = 0
    for c in lst[1:]:
        if c != var:
            var = c
            cnt += 1
    return cnt


lst = list(map(str, input().split()))
x = [c for c in lst if c in ('E', 'W')]
y = [c for c in lst if c in ('N', 'S')]
print(revisits(x), revisits(y))
