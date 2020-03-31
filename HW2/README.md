# 第一題： 求YTM
## 學習歷程

由上課內容與網路查詢可以得知，到期收益率YTM的定義為將債券持有至到期日所能獲得的全部收益利率

並且，還能由本課程第三次授課講義第七頁得公式如下

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula1.PNG"/>

其中

PV: 售價 (Current Bond Price)

F: 票面價格 (Bond Par Value)

m: 每年付息次數 (Number of Payments per year)

C: Fc⁄m，其中c為息票率 (Annual Coupon Rate)

n: 總支付次數 (Number of Cash Flows) = m × Yeas to Maturity

r: 到期收益率 (Yield to Maturity (YTM))

在給定售價、票面價格、每年付息次數、息票率、總支付次數或年數的情況下，可以藉由將各參數帶入上述公式計算求得到期收益率(YTM)。但由於未知數YTM在∑內部，難以直接藉由移項求得，因此我們先將PV的計算以函數表示，接著以迴圈令YTM由0.000001開始以每單位0.000001往上遞增計算PV，使計算的PV與使用者輸入之PV進行相減，當差距小到一定程度時，該YTM即為所求。

又課程提供之範例網站如下：https://www.calkoo.com/en/ytm-calculator

本題程式寫作架構與範例網站大致相似，惟Number of Payments per year範例網站是以選項式呈現，但為了保留更多彈性，這題的程式會請使用者自行輸入一年內支付利息的次數進行計算。

## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/flowchart1.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install matplotlib和輸入pip install numpy，安裝本程序所需之函式庫，執行程式

```typescript
PV = float(input("Current Bond Price(PV): "))
F = float(input("Bond Par Value(F): "))
m = int(input("Number of Payments per year(m): "))
c = float(input("Annual Coupon Rate(c)(%): "))/100
yr = float(input("Yeas to Maturity(yr): "))
C = F*c/m  # 每期付息
n = int(m*yr)  # 總期數(總支付次數)

def Calculate_PV(r):
    capital = F/((1 + r/m)**n)  # 計算到期時所能拿回的本金
    interest = 0  # 計算每期利息加總
    for i in range(1, n + 1):
        interest += float(C/((1 + r/m)**i))
    return (interest + capital)
    
r = 0
while r <= 1:
    r += 0.000001  # r不斷遞增至算出的PV = 真實PV
    FakePV = Calculate_PV(r)
    if abs(FakePV - PV) <= 0.001:
        YTM = round(r*100/m, 4)
        break

print(str(YTM) + "%")
```

# 第二題： 求Spot Rate
## 學習歷程

在網站與上課講義搜尋即期利率Spot Rate的定義為在某一給定時間點上零息債券的到期收益率YTM

課程提供之範例網站如下：https://www.trignosource.com/finance/spot%20rate.html#Calculator

由本課程第三次授課講義第十九頁可得公式如下

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula2.PNG"/>


其中

PV: 售價 (Current Bond Price)

S(i): 即期利率 (Spot Rate)

i: 到期年數 (Duration of Spot Rate)

將公式移項整理成

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula3.PNG"/>

在使用者輸入到期年數i與售價PV後，可求得即期利率S(i)

又根據範例網站，欲求得連續即期利率Continuous Spot Rate (Y(i))

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula4.PNG"/>

將公式移項整理成

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula5.PNG"/>

在使用者輸入到期年數i與售價PV後，可求得即期利率Y(i)

## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/flowchart2.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install matplotlib和輸入pip install numpy，安裝本程序所需之函式庫，執行程式

```typescript
import math
i = float(input("Duration of Spot Rate(i)(years): "))
PV = float(input("Current Bond Price(PV): "))  # 僅能輸入 0~1 之中數值

Si = (PV**(-1/i) - 1)*100  # Spot Rate
print(str(round(Si, 2)) + "%")

Yi = ((-1/i)*math.log(PV))*100  # Continuous Spot Rate
print(str(round(Yi, 2)) + "%")
```



# 第三題： 求Forward Rate
## 學習歷程

遠期利率Forward Rate為在給定的即期利率中，市場所預期的未來某一段時間內利率

課程提供之範例網站如下：https://www.trignosource.com/finance/Forward%20rate.html#Calculator

由講義與網站查詢

(http://greenhornfinancefootnote.blogspot.com/2010/08/how-to-compute-forward-rates-from.html)

後可以得知，下式中的”距今半年的半年遠期利率”為我們要的答案，可以藉由已知的一年期與半年期即期利率計算而得。

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula6.PNG"/>

將上述公式經過移項整理，可在本課程第三次授課講義第二十五頁得公式如下

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula7.PNG"/>


其中

F(i, j): 遠期利率 (Forward Rate)

i: 到期年數 (Duration of Spot Rate)

j: 到期年數 (Duration of Spot Rate)

S(i):  i年期即期利率 (Spot Rate in i years)

S(j):  j年期即期利率 (Spot Rate in j years)

在使用者輸入所需參數後，可以求得遠期利率Forward Rate

## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/flowchart3.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install matplotlib和輸入pip install numpy，安裝本程序所需之函式庫，執行程式

```typescript
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

```




# 第四題： 建立 Forward Rate 對照表

## 學習歷程

由第三題範例網站：https://www.trignosource.com/finance/Forward%20rate.html#Calculator
可得到公式

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/formula8.PNG"/>

在使用者輸入Duration和每期價格後可以雙層迴圈求得Forward rate的二階陣列表，接著用matplotlib繪製表格

## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW2/image/flowchart4.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install matplotlib和輸入pip install numpy，安裝本程序所需之函式庫，執行程式

```typescript
import numpy as np
import matplotlib.pyplot as plt
import math

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
```
