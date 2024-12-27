## Uncertainty.py
### == sd

import numpy as np

# Uncertainty() function -> How to find the standard deviation
def sd(N, mean, x):  # N: count, mean: mean, x: list
    total_sum = 0
    for i in range(N):
        total_sum += (x[i] - mean) ** 2
    sig = np.sqrt(total_sum / (N - 1))
    return sig

N = int(input(f'Input N (number of data points): '))
mean = float(input(f'Input mean: '))
x = list(map(float, input(f'Input x list (comma-separated): ').split(',')))

if len(x) != N:
    print("Error: Length of x list does not match N.")
else:
    result = sd(N=N, x=x, mean=mean)
    print(f"Standard Deviation: {result}")
