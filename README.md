# Monte_Carlo_Simulation

A Monte Carlo simulation is an attempt to predict the future many times over. At the end of the simulation, thousands or millions of "random trials" produce a distribution of outcomes that can be analyzed.
The distribution of final prices at a future point in time turns out to converge to a normal distribution or bell-curve distribution. All random events in nature tend to being a normal distribution at infinite trials.
This hypothesis is verified by the output.

I have bulit a model which assumes that at each time step the price of the stock moves randomly with maximum change in value equal to the volatility(which is taken to be a constant for simplification). Hence the price at each step changes to random number between [previous_price(1-volatility) , previous_price(1+volatility)].

