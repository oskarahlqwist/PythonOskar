import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv('data_by_genres.csv', sep = ',', encoding='utf-8')
df.plot(kind = 'scatter', x = 'tempo', y = 'energy', alpha = a)
plt.show()