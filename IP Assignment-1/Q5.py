def fact(x):
    fact = 1
    for i in range(0, x-1):
        fact *= (x-i)
    return fact


def sin(x):
    sum = 0
    for i in range(1, 21):
        sum += ((x**((2*i)-1))/(fact((2*i)-1)))*((-1)**(i+1))
    return sum


def cos(x):
    sum = 0
    for i in range(0, 20):
        sum += ((x**(2*i))/fact((2*i)))*((-1)**(i))
    return sum


angle_deg = float(input("enter angle in degrees: "))
angle_rad = (angle_deg*3.14)/180
distance = float(input("enter horizontal distance: "))
height = distance*(sin(angle_rad)/cos(angle_rad))
print("height is :", height)
print("length of line from person to top of the pole is :",
      ((height**2)+(distance)**2)**(0.5))
