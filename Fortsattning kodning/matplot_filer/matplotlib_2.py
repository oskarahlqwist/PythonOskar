import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,3,3,3,4,2,1]

plt.hist(x, bins = 10)
plt.show()






"""
np.random.seed(19680201) ###Ge ett pseudo nummer för att simulera randomness.
N_values = 255
n_bins = 5  ###

mu, sigma = 200, 25
x = mu + sigma * np.random.randn(N_values)


plt.hist(x, n_bins, density=True)

plt.xlabel('Värde')
plt.ylabel('Sannolikhet')
plt.title('Histogram med normalfördelning')
plt.show()"""