# https://www.hackerrank.com/contests/ip-lab7-wednesday/challenges/l7-q5-longest-ss/submissions/code/1354523256

s = input()
dict = {}
L = []
max_len = 0
for i in range(len(s)):
    if s[i] not in dict:
        dict[s[i]] = i
        max_len += 1
    else:
        L += [max_len]
        if i-dict[s[i]] <= max_len:
            max_len = i-dict[s[i]]
        else:
            max_len += 1
        L += [max_len]
        dict[s[i]] = i
    if i == len(s)-1:
        L += [max_len]
print(max(L))
