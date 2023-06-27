def demand(a, b, p):
    return (2.7183**((a-b*p)))


def supply(c, d, p):
    return (2.7183**((c+d*p)))


p = 1.0
a = 10
b = 1.05
c = 1
d = 1.06

dem = demand(a, b, p)
sup = supply(c, d, p)
if dem > sup:
    while dem > sup:
        p = 1.05*p
        dem = demand(a, b, p)
        sup = supply(c, d, p)
elif dem < sup:
    while dem < sup:
        p = 1.05*p
        dem = demand(a, b, p)
        sup = supply(c, d, p)
print("Equilibrium Price is: ", round(p, 2))
print("Items Produced: ", round(sup))
print("Items bought: ", round(dem))
