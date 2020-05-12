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

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW5/image/4.png"/>

輸出結果

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW5/image/5.png"/>

<img src="https://github.com/jenny56402/Financial_Engineering/blob/master/HW5/image/6.png"/>


## 程式碼
```typescript
import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np

X = int(input("strike price: "))  # 履約價
r = float(input("risk-free interest(year): "))
time = float(input("duration of option(year): "))
timestep = int(input("time step: "))
a = float(input("the value of Hull-White Model: "))
sigma = float(input("fluctuation in Hull-White Model: "))  # 波動度
forward_rate = float(input("forward rate: "))
S = int(input("current price: "))
num_paths = int(input("number of simulation paths: "))

day_count = ql.Thirty360()
today = ql.Date().todaysDate()
ql.Settings.instance().evaluationDate = today
spot_curve = ql.FlatForward(today, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)
hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, time, timestep, rng, False)
def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr

t, paths = generate_paths(num_paths, timestep)
plt.figure()
plt.subplot(2,1,1)
for i in range(num_paths):
    plt.plot(t, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")

def genBrownPath (T, mu, sigma, S0, dt):
    n = len(mu)
    t = np.linspace(0, T, n)
    W = [0] + np.random.standard_normal(size = n)
    W = np.cumsum(W)*np.sqrt(dt)
    S = S0*np.exp((mu-0.5*sigma**2)*t + sigma*W )
    plt.plot(t, S)
    return S
call_price_sum = 0
put_price_sum = 0
plt.subplot(2,1,2)
plt.title("Stock Price Simulation by ")
for i in range(num_paths):
    price = genBrownPath(time, paths[i], sigma, S, 1/timestep)
    payoff = price[-1]
    print("payoff path %d: %f"% (i, payoff))
    if payoff >= X:
        call_price_sum += price[-1] - X
    else:
        put_price_sum += X - price[-1]
print("call:", round(call_price_sum / num_paths * np.exp(-r * time), 3))
print("put:", round(put_price_sum / num_paths * np.exp(-r * time),3))
plt.show()
