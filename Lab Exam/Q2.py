# Write a function that returns: median salary, average of salaries of those students whose salary
# is < than median, average of salaries of those students whose salary is >= median


def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2)-1]+lst[(n//2)])/2
    else:
        return lst[((n+1)//2)-1]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_med = []
greater_than_med = []
med = median(l)

for c in l:
    if c < med:
        less_than_med.append(c)
    else:
        greater_than_med.append(c)

avg_less_than_med = sum(less_than_med)/len(less_than_med)
avg_greater_than_med = sum(greater_than_med)/len(greater_than_med)

print(f"median salary is {med}")
print(f"average salary for less than median is {avg_less_than_med}")
print(f"average salary for greater than median is {avg_greater_than_med}")
