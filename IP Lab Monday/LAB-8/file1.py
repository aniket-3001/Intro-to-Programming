'''
A file has many x, y l representing points in an x-y plane. Each pair of l is in one line.
Write a program that will try to fit a regression line on these x-y l (i.e. y = a*x + b). 
Find a and b for this line, and the correlation coefficient. 
Write these in a file. You can call your input file as xy.txt and output file as regression.txt. 
For regression and correlation coefficient, use any standard formulae.
Suggestion: It seems natural to read the l as a list of tuples. 
For creating the input file:
you can randomly select x, use some slope to determine y (as x*slope) and then multiply this y with a random number within a range to "scatter" them (e.g. multiply by a random number between 1 and 1.5)
'''
import random
import matplotlib.pyplot as plt

n = 50
slope = 0.5

scatter_range = (1, 1.5)

x = [random.randint(1, 100) for _ in range(n)]
y = [x[i] * slope * random.uniform(scatter_range[0],
                                   scatter_range[1]) for i in range(n)]

with open('xy.txt', 'w') as f:
    for i in range(n):
        f.write(f"{x[i]}, {y[i]}\n")


def mean(l):
    return sum(l)/len(l)


def variance(l):
    sum_sq_diff = sum([(x - mean(l)) ** 2 for x in l])
    return sum_sq_diff / (len(l) - 1)


def covariance(l1, l2):
    sum_prod = sum([(l1[i] - mean(l1)) * (l2[i] - mean(l2))
                   for i in range(len(l1))])
    return sum_prod / (len(l1) - 1)


def std_dev(l):
    variance = sum((x - mean(l)) ** 2 for x in l) / len(l)
    return (variance)**0.5


L = []
x = []
y = []

with open("xy.txt") as f:
    for line in f:
        t = tuple([float(c) for c in line.split(', ')])
        x += [t[0]]
        y += [t[1]]
        L += [t]

a = covariance(x, y) / variance(x)
b = mean(y) - a * mean(x)
r = covariance(x, y)/(std_dev(x)*std_dev(y))

if b > 0:
    print(f"line of best fit is: y = ({a})x +{b}")
else:
    print(f"line of best fit is: y = ({a})x {b}")

plt.title("Plot")
plt.scatter(x, y)
plt.ylabel("y-axis")
plt.xlabel("x-axis")

line = [a*xi + b for xi in x]
plt.plot(x, line, 'r')

plt.show()
