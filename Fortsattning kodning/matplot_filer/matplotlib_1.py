import matplotlib.pyplot as plt 
import numpy as np

x = np.array([0, 100])
x2 = np.array([0, 50])
x3 = np.array([0, 200])
xaxeln = np.array([0, 250])

plt.plot(xaxeln, x, label="1", c = '#00fb00')
plt.plot(xaxeln, x2, label="2", c = '#ff00ff')
plt.plot(xaxeln, x3, label="3", c = 'Black')


plt.xlabel("X-axeln")
plt.ylabel("Y-axeln")
plt.title("Mitt diagram")

plt.legend()
plt.show()
