# Black-Scholes 選擇權評價模型
## 學習歷程

這次的作業跟兩次相比簡單滿多的，由上課內容與網路查詢可以得知，Black-Scholes 選擇權評價模型可被用來計算理論上選擇權的目前價值

我們能從本課程第七次中得到計算call price & put price的公式如下：

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/1.PNG"/>

其中

c: call price

p: put price

N(.): normal distribution function

S: current stock price

X: strike price

r: interest rate

T: time to maturity (year)

σ: Volatility (year)


計算normal distribution 內部數值 (d_1  & d_2) 的公式如下:

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/2.PNG"/>

因此在輸入所需參數的資料後，即可由上述公式得出call price & put price

但這次作業有利息給付的問題，因此我們需要將上式中的S修正為 S ̂ 

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/3.PNG"/>

其中

D: riskless dividends paid during the life of the option

S ̂: expected present value of both capital gains and other risky dividends

而D的計算公式為

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/4.PNG"/>

其中

div: dividends

mon: pay month (在第幾個月付息)


也就是將所有付息月份套入此計算公式並且相加即可得D


## 流程圖

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW4/image/5.PNG"/>

## 程式碼與執行方法

下載Python3.7，電腦螢幕左下角”開始”按右鍵，按執行，輸入cmd並確認，輸入pip install scipy，安裝本程序所需之函式庫，執行程式

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


```
