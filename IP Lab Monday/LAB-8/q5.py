import ast
s = input()
cnt = 0
dict = ast.literal_eval(s)

for c in list(dict.values()):
    for d in c:
        cnt += 1

l = []
for i in range(cnt):
    l += [0]

for key, value in dict.items():
    for c in value:
        l[c] = key

print(l)
