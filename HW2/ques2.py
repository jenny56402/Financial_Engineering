import math
i = float(input("Duration of Spot Rate(i)(years): "))
PV = float(input("Current Bond Price(PV): "))  # 僅能輸入 0~1 之中數值

Si = (PV**(-1/i) - 1)*100  # Spot Rate
print(str(round(Si, 2)) + "%")

Yi = ((-1/i)*math.log(PV))*100  # Continuous Spot Rate
print(str(round(Yi, 2)) + "%")