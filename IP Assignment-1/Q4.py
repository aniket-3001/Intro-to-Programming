import math


def vel(t):
    v = 2000*math.log(140000/(140000-(2100*t)))-(9.8*t)
    return v


a = float(input("enter starting time in seconds: "))
b = float(input("enter ending time in seconds: "))
t = a
dt = 0.25
dist = 0
while t < b:
    dist += (vel(t)+vel(t+dt))*(dt/2)
    t += dt
print("distance travelled is:", dist)
