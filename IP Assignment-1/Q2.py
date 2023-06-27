def calc_prof(no_tables, no_chairs, m):
    if no_tables <= m:
        profit_tables = no_tables * 90
    else:
        profit_tables = (90 * m) + ((no_tables - m) * 100)
    if no_chairs <= m:
        profit_chairs = no_chairs * 25
    else:
        profit_chairs = (25 * m) + ((no_chairs - m) * 30)
    total_profit = profit_tables + profit_chairs
    return total_profit


def max_no_tables(assem_lab_hrs_per_table, fin_lab_hrs_per_table, assem_max_lab_hrs, fin_max_lab_hrs):
    if assem_max_lab_hrs // assem_lab_hrs_per_table >= fin_max_lab_hrs // fin_lab_hrs_per_table:
        return int(fin_max_lab_hrs // fin_lab_hrs_per_table)
    else:
        return int(assem_max_lab_hrs // assem_lab_hrs_per_table)


def max_no_chairs(assem_lab_hrs_per_chair, fin_lab_hrs_per_chair, assem_max_lab_hrs, fin_max_lab_hrs):
    if assem_max_lab_hrs // assem_lab_hrs_per_chair >= fin_max_lab_hrs // fin_lab_hrs_per_chair:
        return int(fin_max_lab_hrs // fin_lab_hrs_per_chair)
    else:
        return int(assem_max_lab_hrs//assem_lab_hrs_per_chair)


m = int(input("enter M: "))
assembly_max = 400
finishing_max = 120
assembly_table = 8
finishing_table = 2
assembly_chair = 2
finishing_chair = 1
x1 = max_no_tables(assembly_table, finishing_table,
                   assembly_max, finishing_max)
x2 = max_no_chairs(assembly_chair, finishing_chair,
                   assembly_max, finishing_max)
max_profit = 0
for i in range(0, x1+1):
    for j in range(0, x2+1):
        if (assembly_table*i)+(assembly_chair*j) <= assembly_max and (finishing_table*i)+(finishing_chair*j) <= finishing_max:
            profit = calc_prof(i, j, m)
            if profit > max_profit:
                max_profit = profit
                no_tables = i
                no_chairs = j
print("no. of chairs is: " + str(no_chairs))
print("no. of tables is: " + str(no_tables))
print("maximum profit is: $" + str(max_profit))
