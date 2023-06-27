def fn(x):
    return ((x**3)+2)/((x**2)+1)


def integrate(a, b, dx=0.00001):
    area = 0
    x_coor = a
    while x_coor <= b:
        y_coor = fn(x_coor)
        area += y_coor*dx
        x_coor += dx
    return area


start = float(input("enter start value of interval: "))
end = float(input("enter end value of interval: "))
area = integrate(start, end)
print(area)
