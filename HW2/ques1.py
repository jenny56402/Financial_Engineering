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