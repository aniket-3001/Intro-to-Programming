x0, y0 = 5, 5
x, y = x0, y0
tot_dist = 0
while True:
    dist = int(input("enter distance vehicle has to travel: "))
    if dist <= 0:
        break
    elif dist <= 25:
        y += dist
    elif dist <= 50:
        y -= dist
    elif dist <= 75:
        x += dist
    else:
        x -= dist
    tot_dist += dist
disp = ((x-x0)**2+(y-y0)**2)**0.5
print("final coordinates: "+'('+str(x)+','+str(y)+')')
print("total distance travelled: "+str(tot_dist)+" units")
print("straight line distance between final and initial positions: "+str(disp)+" units")
