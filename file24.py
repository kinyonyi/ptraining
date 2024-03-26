import matplotlib.pyplot as plt 
import numpy as np
plt.style.use("fivethirtyeight")

x = np.arange(10)
y1 = np.square(x)
y2 = np.sqrt(x)

plt.title("A graph")
plt.xlabel("x values")
plt.ylabel("y values")

plt.plot(x, y1, label="x against squares")
plt.plot(x, y2, label="x against sqrt")
plt.legend()

plt.show()