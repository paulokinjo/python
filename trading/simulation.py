import random
from math import exp, sqrt
S0 = 100
r = 0.05
T = 1.0
sigma = 0.2

values = []

for _ in range(1000000):
  ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * random.gauss(0, 1) * sqrt(T))
  values.append(ST)