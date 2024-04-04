#scatter graph
import matplotlib.pyplot as plt 
import numpy as np

plt.style.use("fivethirtyeight")

"""
x = np.random.randn(100)
y = np.random.randn(100)
sizes = np.random.randint(low=20, high=100, size=100)
colors = np.random.randint(low=100, high=200, size=100)
"""
x = [5,4,6,8,6,5,4]
y = [2,4,3,7,9,3,2]
sizes = [190, 110, 200, 190, 150, 90, 70]
colors = [30, 10, 90, 60, 50, 30, 60]


plt.scatter(x, y, s=sizes, c=colors, cmap="Greens", label="random generated values")

cbar = plt.colorbar(label = "Satisfaction Rate!")

plt.title("scatter graph for x values")
plt.legend()
plt.xlabel("x random values")
plt.ylabel("y random values")
plt.grid(True)
plt.tight_layout()

plt.show()