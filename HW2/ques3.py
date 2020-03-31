import math
t = int(input("Time due for the beginning of forward rate(years): "))
r = int(input("Duration of forward rate(years): "))
yt = float(input("Price of " + str(t) +" year unit zero coupon bond: "))
ytr = float(input("Price of " + str(t + r) + " year unit zero coupon bond: "))
print("")
f = (yt / ytr)**(1/r) - 1
print(str(r) + " year forward rate of interest beginning " + str(t) + " years from now: " + str(round(f * 100, 2)) + " %")
F = math.log(f + 1)
print(str(r) + " year forward force of interest beginning " + str(t) + " years from now: " + str(round(F * 100, 2)) + " %")
