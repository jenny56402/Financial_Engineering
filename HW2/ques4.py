import numpy as np
import matplotlib.pyplot as plt
import math
"""
t = int(input("Time due for the beginning of forward rate(years): "))
r = int(input("Duration of forward rate(years): "))
yt = float(input("Price of " + str(t) +" year unit zero coupon bond: "))
ytr = float(input("Price of " + str(t + r) + " year unit zero coupon bond: "))
print("")   
f = (yt / ytr)**(1/r) - 1
print(str(r) + " year forward rate of interest beginning " + str(t) + " years from now: " + str(round(f * 100, 2)) + " %")
F = math.log(f + 1)
print(str(r) + " year forward force of interest beginning " + str(t) + " years from now: " + str(round(F * 100, 2)) + " %")
"""
# i = t
# j = t + r, r = j - i

y = []
period = int(input("Period: "))

for i in range(period):
    y.append(float(input("Current Bond Price(PV) of period "+ str(i) + ": ")))
table = []
for i in range(period):
    tmp = []
    for j in range(period):
        tmp.append(0)
    for j in range(i + 1, period):
        tmp[j] = round((y[j] / y[i])**(1 / (j - i)) - 1, 4)
    table.append(tmp)

for i in range(period):
    for j in range(period):
        print("%7s" % table[i][j], end = " ")
    print("")

columns = ['%d year' % x for x in range(period)]
rows = ['%d year' % x for x in range(period)]


the_table = plt.table(cellText=table,
                      rowLabels=rows,
                      colLabels=columns,
                      loc="center")
plt.axis('off')

plt.show()