#plotting of graphs
#Ensure to have matplot lib installed

import matplotlib.pyplot as plt 
import numpy as np

print(plt.style.available)
plt.style.use("fivethirtyeight")

x = np.linspace(0,10,20)
y = [z**2 for z in x]
z = [z**3 for z in x]

plt.title("A graph of x against x**2")
plt.xlabel("x values")
plt.ylabel("y values")

"""
'.': Point marker
',': Pixel marker
'o': Circle marker
'v': Downward-pointing triangle marker
'^': Upward-pointing triangle marker
'<': Left-pointing triangle marker
'>': Right-pointing triangle marker
'1', '2', '3', '4': Triangular markers pointing downward, leftward, upward, and rightward respectively
'p': Pentagram marker
'H': Hexagon marker
'+': Plus marker
'x': Cross (x) marker
'D': Diamond marker
'd': Thin diamond marker
"""

plt.plot(x, y, label="x against y", color="red", marker="o", linewidth="4")
plt.plot(x, z, label="x against z", marker="H", linestyle="dotted")
plt.legend()

#saving of the graph 
plt.savefig("myPlot")

plt.show()

