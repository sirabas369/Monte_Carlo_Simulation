import numpy as np
import random
import matplotlib.pyplot as plt

timesteps = 30
max_simulations = 5000
volatility = 2
starting_price = 600.00

paths = np.full(( timesteps+1 , max_simulations), starting_price)
paths[0][:] = starting_price

for i in range (0,max_simulations):
    for j in range(1 , timesteps+1):
        low = paths[j-1][i]*(1-(volatility/100))
        high = paths[j-1][i]*(1+(volatility/100))
        paths[j][i] = random.uniform(low , high)

last_prices = paths[timesteps][:]

plt.figure(1)
plt.plot(paths)
plt.title("line graph")
plt.xlabel("day")
plt.ylabel("prices")

plt.figure(2)
plt.hist(last_prices, bins = 90)
plt.title("Histogram")
plt.xlabel("Price")
plt.ylabel("Occurences")
plt.show()
