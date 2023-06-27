def check_power_of_2(num):
    return num & num-1 == 0


l = list(map(int, input().split()))
cnt = 0
for c in l:
    if check_power_of_2(c):
        cnt += 1

print(cnt)

# another approach is to count set bits...no. of set bits should be 1
