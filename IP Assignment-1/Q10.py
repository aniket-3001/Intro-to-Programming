def polynomial(x):
    polynomial = x**3-10.5*x**2+34.5*x-35
    return polynomial


def slope(x):
    slope = 3*(x**2)-21*x+34.5
    return slope


def zerocheck(polynomial, x0):
    for i in range(100):
        poly_val = polynomial(x0)
        if poly_val >= -0.2 and poly_val <= 0.2:
            return x0
        slope_val = slope(x0)
        x0 -= poly_val/slope_val
    return 9999  # if no root found


roots = []
x1 = int(input("Enter start range: "))
x2 = int(input("Enter end range: "))
for i in range(x1, x2+1):
    root = 0
    root = round(zerocheck(polynomial, i), 1)
    if root != 9999 and root not in roots:
        roots += [root]
if len(roots) != 0:
    print("The roots in given range are: ", end='')
    for c in roots:
        print(c, end=' ')
else:
    print("No roots exist in given range.")
