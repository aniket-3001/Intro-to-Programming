def name_hundred(n):
    if n >= 0 and n <= 99:
        dig = n % 10
        n = n//10
        if n == 1:
            if dig == 0:
                print("ten", end="")
            elif dig == 1:
                print("eleven", end="")
            elif dig == 2:
                print("twelve", end="")
            elif dig == 3:
                print("thirteen", end="")
            elif dig == 5:
                print("fifteen", end="")
            else:
                print(units(dig) + "teen", end="")
        elif n == 2:
            print("twenty " + units(dig), end="")
        elif n == 3:
            print("thirty " + units(dig), end="")
        elif n == 4:
            print("forty " + units(dig), end="")
        elif n == 5:
            print("fifty " + units(dig), end="")
        elif n == 6:
            print("sixty " + units(dig), end="")
        elif n == 7:
            print("seventy " + units(dig), end="")
        elif n == 8:
            print("eighty " + units(dig), end="")
        elif n == 9:
            print("ninety " + units(dig), end="")
        elif n == 0:
            if dig == 0:
                print("zero", end="")
            else:
                print(units(dig), end="")


def units(dig):
    if dig == 1:
        return ("one")
    elif dig == 2:
        return ("two")
    elif dig == 3:
        return ("three")
    elif dig == 4:
        return ("four")
    elif dig == 5:
        return ("five")
    elif dig == 6:
        return ("six")
    elif dig == 7:
        return ("seven")
    elif dig == 8:
        return ("eight")
    elif dig == 9:
        return ("nine")
    elif dig == 0:
        return ("")


n = int(input("enter number which is to be displayed in words: "))
if n > 0:
    less = n % 100
    n = n//100
    hundreds = n % 10
    n = n//10
    thousands = n % 100
    n = n//100
    lacs = n % 100
    n = n//100
    crores = n % 100
    n = n//100

    if n > 0:
        print("Number greater than 9 digits")
    else:
        if crores > 0:
            name_hundred(crores)
            print(" crore", end=" ")
        if lacs > 0:
            name_hundred(lacs)
            print(" lac", end=" ")
        if thousands > 0:
            name_hundred(thousands)
            print(" thousand", end=" ")
        if hundreds > 0:
            name_hundred(hundreds)
            print(" hundred", end=" ")
        if less > 0:
            name_hundred(less)
else:
    print("zero")
