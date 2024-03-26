#plotting of graphs
#Ensure to have matplot lib installed

import matplotlib.pyplot as plt 
import numpy as np

print(plt.style.available)
plt.style.use("fivethirtyeight")

x = np.linspace(0,10,20)
y = [z**2 for z in x]
z = [z**3 for z in x]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))#figsize=(10,4) returns inches
#plt.figure(figsize=(8,5))

#graph ax1
ax1.set_title("A graph of x against x**2", fontsize = 12, color = "red")
ax1.set_xlabel("x values")
ax1.set_ylabel("y values")
ax1.plot(x, y, label="x against y")

#graph ax2
ax2.set_title("A graph of x against x**3", fontsize = 12, color = "red")
ax2.set_xlabel("x values")
ax2.set_ylabel("z values")
ax2.plot(x, z, label="x against z")

plt.legend()
plt.tight_layout()
plt.savefig("myPlot")
plt.show()


"""
plot a graph, wc will have x values from 0 to 10
y1 values -> quares of the x values
y2 values -> sqrt of the x values
label the lines
have a title to the graph 
save it as plot1.png
"""

