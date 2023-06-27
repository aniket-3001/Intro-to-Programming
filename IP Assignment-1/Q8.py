def pop_after_n(ini_pop, r, n):
    pop = ini_pop
    for i in range(n):
        inc = (pop*r)/100
        pop += inc
        r -= 0.1
    return pop


pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
cur_pop = sum(pop)
print("current population: " + str(cur_pop) + " millions")
max_pop = cur_pop
year = 0
while max_pop >= cur_pop:
    r = 2.5
    cur_pop = max_pop
    max_pop = 0
    year += 1
    for i in pop:
        max_pop += pop_after_n(i, r, year)
        r -= 0.4
print("maximum population will be " + str(cur_pop) +
      " millions reached after " + str(year-1) + " years")
