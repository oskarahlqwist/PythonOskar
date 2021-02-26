import matplotlib.pyplot as plt 
import pandas as pd

data = pd.read_csv(r'D:\Kodning\Python projekt\Fortsattning kodning\matplot_filer\data_by_genres.csv')
df = pd.DataFrame(data, columns= ['genres','energy'])
print(df)

