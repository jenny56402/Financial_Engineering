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