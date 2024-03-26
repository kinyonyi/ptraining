import matplotlib.pyplot as plt 
import numpy as np
plt.style.use("fivethirtyeight")

x = [120, 50, 40, 80, 90, 100]
labels = ["Mbale","Kampala","Jinja","Mbarara","Kapchorwa","Lira"]
explode = [0.1, 0, 0, 0, 0, 0]
plt.title("A Pie Chart")

plt.pie(
    x,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode,
    startangle=45,
    shadow=True,
    wedgeprops={"edgecolor":"teal", "linewidth":1}
    )

#plt.legend(loc="lower right")
plt.tight_layout()
plt.show()