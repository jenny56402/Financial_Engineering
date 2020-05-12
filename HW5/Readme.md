# Option Pricing with Hull White Model
## 學習歷程

這次作業相對先前複雜些許，以下的計算公式皆出自上課講義與上網查詢

1.	透過Monte Carlo method

A.	對Hull White Model 模擬Short Rate

我們能從本課程第九次講義中得到公式如下：


<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW5/image/1.PNG"/>


其中θ 由利率期限結構曲線計算而來，a為外部給定參數

程式部分參考：http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html


B.	將Short Rate帶入Geometric Brownian Motion，r換成r(t)模擬股價

由網站查詢可得公式如下：


<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW5/image/2.PNG"/>

將上一小題所計算得Short rate帶入可計算得r(t)

程式部分參考：http://nordtyped.de/generating-random-paths-using-geometric-brownian-motion-with-python/

C.	自訂選擇權履約價，對每一條path計算出到期日時的PayOff

以蒙地卡羅法進行計算，設定path數量為200


2.	對所有Path的PayOff進行期望值計算，並折現回t = 0的時間點


3.	計算出Call Price & Put Price

帶入計算完畢後，繪製走勢圖






## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW5/image/3.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install matplotlib.pyplot，輸入pip install numpy，輸入pip install QuantLib以安裝本程序所需之函式庫，執行程式

## 執行結果 (以範例參數為例)

輸入題目的範例參數

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/6.png"/>

輸出結果

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/7.png"/>


## 程式碼
```typescript
import math
from scipy import stats

S = int(input("current price: "))
sigma = float(input("fluctuation: "))  # 波動度
period = int(input("periods(/year): "))  # 一年的期數
dividend = float(input("dividends: "))  # 每期股利
r = float(input("return rate: "))
X = int(input("strike price: "))  # 履約價
T = float(input("maturity period(year): "))

D = 0
for i in range(period):
    dividend_month = int(input("dividend month: "))  # 在第幾月付息
    D += dividend*math.exp(-r*dividend_month/12)

S_hat = S - D

d1 = (math.log(S_hat/X) + (r + 0.5*(sigma**2))*T)/(sigma*(T**0.5))
d2 = d1 - sigma*(T**0.5)

c = S_hat*stats.norm.cdf(d1) - X*math.exp(-r*T)*stats.norm.cdf(d2)
p = c + X*math.exp(-r*T) - S_hat

print("call price: " + str(round(c, 2)))
print("put price: " + str(round(p, 2)))
