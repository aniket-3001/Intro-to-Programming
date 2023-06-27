# https://www.hackerrank.com/contests/lab-4-monday/challenges/lab-4bonus-1-easy-pattern

n = int(input())
for i in range(n, 0, -1):
    print('', end=' ')
    stars = n-i+1
    if stars > i:
        print('*'*i, end='')
    else:
        cnt = 0
        while cnt < i:
            if cnt >= i-stars:
                print('*'*(i-cnt), end='')
            else:
                print('*'*stars, end=' ')
            cnt += stars+1
    print()
