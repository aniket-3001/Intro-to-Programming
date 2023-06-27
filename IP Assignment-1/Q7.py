def no_of_months(cost, allowance=20000, sf=0.1, r=0.5):
    saving = allowance*sf
    interest = 0
    tot_sav = 0
    months = 0
    while tot_sav < cost:
        interest = tot_sav*r
        tot_sav += saving+interest
        months += 1
    return months, tot_sav


def sf(cost, months, allowance=20000, r=0.5):
    sav_frac = cost/(allowance*(((1+r)**months)-1)/r)
    return round(sav_frac, 2)


cost = int(input("enter cost of laptop: "))
months, tot_sav = no_of_months(cost)
print("you can purchase laptop after "+str(months)+" month(s)")
print("money left:", round((tot_sav-cost), 2))
print()
print("Saving Fractions in case you wish to purchase the laptop earlier:\n")
print("Months ", "Saving Fraction")
i = months
while i >= 1:
    sav_frac = sf(cost, i)
    if sav_frac <= 1:
        print(i, "\t", sav_frac)
    else:
        print(i, "\t", "Not possible")
    i -= 1
