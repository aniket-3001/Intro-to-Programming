def diffrentiation(lst, x):
    diff_poly = 0
    for i in range(len(lst)):
        diff_poly += (lst[i]*i)*(x**(i-1))
    return diff_poly


poly_list = list(
    map(int, input("enter space separated values for polynomial: ").split()))
a = float(input("enter point at which you  wish to calculate the slope: "))

slope = diffrentiation(poly_list, a)
print("slope of polynomial at point", a, "is", slope)
