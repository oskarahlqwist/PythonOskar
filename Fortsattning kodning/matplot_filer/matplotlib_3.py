import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = "D:\Kodning\Python projekt\Fortsattning kodning\matplot_filer\data_by_genres.csv"

df = pd.read_csv(data)

df.head(3)



"""
df = pd.read_csv(data, sep = ',', encoding='utf-8')

df.plot(kind = 'scatter', x = 'tempo', y = 'energy', alpha = 0.4)

plt.show()"""