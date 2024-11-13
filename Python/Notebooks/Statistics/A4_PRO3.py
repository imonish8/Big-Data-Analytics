import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = { 'Stock_Price': [150, 155, 160, 165, 170, 175, 180, 185, 190, 195], 'Trading_Volume': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000], 'High_Price': [155, 160, 165, 170, 175, 180, 185, 190, 195, 200], 'Low_Price': [145, 150, 155, 160, 165, 170, 175, 180, 185, 190] }
df = pd.DataFrame(data)
print(df)

m = df.corr()
print(m)

sns.heatmap(m, annot=True)

plt.show()