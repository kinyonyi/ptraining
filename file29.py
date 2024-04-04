import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("_classic_test_patch")

df = pd.read_csv('pokemon_data.csv')

speed_counts = df[['Type 1', 'Speed']].groupby(['Type 1']).mean().nsmallest(5, "Speed")
explode = [0.1 if x == np.max(speed_counts['Speed']) else 0 for x in speed_counts['Speed']]

plt.figure(figsize=(6, 4))
plt.pie(
    speed_counts['Speed'],
    labels=speed_counts.index,
    explode=explode,
    wedgeprops={"edgecolor":"white"},
    shadow=True,
    startangle=90,
    autopct='%1.1f%%')
plt.title('Distribution of Pokémon Type 1 by Speed', fontsize = 12, color="green", fontweight=900)
plt.show()