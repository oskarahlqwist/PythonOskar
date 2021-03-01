<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

=======
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv('data_by_genres.csv', sep = ',', encoding='utf-8')
df.plot(kind = 'scatter', x = 'tempo', y = 'energy', alpha = a)
>>>>>>> fa5061e14f49a283fd8984bfa447b3e8e7de17d5
plt.show()