# Binomial Option Pricing Model (BOPM)
## 學習歷程

由上課內容與網路查詢可以得知，可以在得知股票的履約價 (strike price) 與現貨價 (stock price) 的情況下，以存續期間內歷史上漲或下跌比率計算出call price

並且，還能由本課程第五次授課講義第四十四頁得範例如下

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW3/image/1.PNG"/>

### Binomial process for the stock price (由左至右計算)
以stock price ($160) 作為模型起點，向右上方走一步就乘以上漲率 (u = 1.5)，向右下方則乘以下跌 (d = 0.5) ，下方括號處為機率，往右上方乘以 p = (R - d)/(u - d) = 0.7，往右下方則乘以 1 – p (= 0.3)，以範例三期 (n = 3) 為例，則模型走了三次

### Binomial process for the call price (由右至左計算)
將右方模型的計算結果減去履約價 (X = 150)，若是為負數則以0當作計算起點，往左下方乘以p (= 0.7)，往左上方則乘以 1 – p (= 0.3)，但一律要除以 R (= exp(r) = 1.2)若為兩路徑交錯點則將計算結果相加，因範例為三期，故模型也是移動三步，至交錯點 (最左方) 則為所求 (call price)

在使用者輸入現貨價 (S)、上漲率 (u)、下跌率 (d)、無風險利率 (r)、現貨價 (X) 、期數 (n) 的情況下，可以藉由將各參數帶入上述模型計算求得call price。



## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW3/image/2.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install matplotlib和輸入pip install numpy，安裝本程序所需之函式庫，執行程式



## 執行結果 (以範例參數為例)

Stock price: 160
The probability of price increase: 1.5
The probability of price decrease: 0.5
Riskless rate: 0.18232
Strike price: 150
Number of periods:3

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW3/image/3.PNG"/>


```typescript
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


```
