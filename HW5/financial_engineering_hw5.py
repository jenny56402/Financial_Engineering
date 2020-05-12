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