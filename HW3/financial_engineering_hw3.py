import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

s = int(input("Stock price: "))
u = float(input("The probability of price increase: "))
d = float(input("The probability of price decrease: "))
r = float(input("Riskless rate: "))
x = int(input("Strike price: "))
n = int(input("Number of periods: ")) + 1
R = math.exp(r)
p = (R - d)/(u - d)

table = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append((0, 0))
    table.append(tmp)
table[0][0] = s, 1
for i in range(1, n):
    table[0][i] = round(table[0][i-1][0]*u), table[0][i-1][1]*p
    table[i][0] = round(table[i-1][0][0]*d), table[i-1][0][1]*(1-p)
for i in range(1, n):
    for j in range(1, n - i):
        table[i][j] = (round(max(table[i-1][j][0]*d, table[i][j-1][0]*u)),
                       table[i-1][j][1]*(1-p) + table[i][j-1][1]*p)

table2 = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append((0, 0))
    table2.append(tmp)
for i in range(n):
    table2[i][n - i - 1] = (max(0, table[i][n - i - 1][0] - x), i == 0)


for i in range(n):
    for j in range(n - i - 1):
        ii = j
        jj = n - j - i - 2
        table2[ii][jj] = (table2[ii][jj + 1][0] * p + \
                          table2[ii + 1][jj][0] * (1 - p)) / R, \
                         (table2[ii][jj + 1][0] - table2[ii + 1][jj][0]) / \
                         (table[ii][jj + 1][0] - table[ii + 1][jj][0])
                         
                         
print("")

# table1處理(四捨五入)及輸出
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            table[i][j] = "N/A"
        else:
            table[i][j] = table[i][j][0], round(table[i][j][1], 3)
            print(table[i][j], end=" ")
    print("")
# table2處理(四捨五入)及輸出
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            table2[i][j] = "N/A"
        elif i + j == n - 1:
            table2[i][j] = round(table2[i][j][0], 3),
            print(table2[i][j], end=" ")
        else:
            table2[i][j] = round(table2[i][j][0], 3), round(table2[i][j][1], 5)
            print(table2[i][j], end=" ")
    print("")

print("Call price = %.3f" % table2[0][0][0])

columns = ["%d" % x for x in range(1, n + 1)]
rows = ["%d" % x for x in range(1, n + 1)]
plt.subplot(2, 1, 1)
plt.axis('off')    
#plt.rcParams["font.sans-serif"]=["Arial"]

the_table = plt.table(cellText=table,
                      rowLabels=rows,
                      colLabels=columns,
                      loc="center")
the_table.scale(1.2, 1.2)

plt.subplot(2, 1, 2)
plt.axis('off')    

the_table2 = plt.table(cellText=table2,
                      rowLabels=rows,
                      colLabels=columns,
                      loc="center")
the_table2.scale(1.2, 1.2)
plt.show()

