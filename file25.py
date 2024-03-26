import matplotlib.pyplot as plt 
import numpy as np
plt.style.use("fivethirtyeight")

x = np.array([4,10,15,20])
y1 = [x*2 for x in x]
y2 = np.sqrt(x)
y3 = [x*3 for x in x]

plt.title("A graph")
plt.xlabel("x values")
plt.ylabel("y values")

width = 0.25
new_x_values = np.arange(len(x))
print(new_x_values)

plt.bar(new_x_values - width, y1, width=width, label="x against x * 2")
plt.bar(new_x_values, y2, width=width, label="x against sqrt")
plt.bar(new_x_values + width, y3, width=width, label="x against x * 3")
plt.legend()
plt.xticks(ticks=new_x_values, labels=x)
plt.tight_layout()
plt.show()