#histogram

import matplotlib.pyplot as plt 
import numpy as np

plt.style.use("fivethirtyeight")
"""
x = np.random.randn(1000)
myBins = [-3,-2,-1,0,1,2,3]
"""
x = [19,30,20,40,60,30,25]
myBins = [10,20,30,40,50,60]

mean_value = np.mean(x)
median_value = np.median(x)
print(mean_value, median_value)

plt.hist(x, bins=myBins, label="ages", edgecolor = "white")

plt.text(mean_value + 0.4, 1, f"The Mean Value is {mean_value:.4f}", color = "red", fontsize=12, va='top')
plt.text(median_value + 0.4, 1.4, f"The Median Value is {median_value:.4f}", color = "blue", fontsize=12, va='top')

plt.axvline(mean_value, linewidth=2, color = "red", label="Mean Value")
plt.axvline(median_value, linewidth=2, color = "blue", label = "Median Value")

plt.title("ages obtained during some survey")
plt.xlabel("ranges")
plt.ylabel("frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
