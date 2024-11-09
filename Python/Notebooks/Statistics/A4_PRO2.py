import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas.core.reshape.reshape import unstack

data = { 'Price': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550], 'Quality': [4, 5, 6, 7, 8, 9, 9, 10, 10, 9], 'Design': [3, 5, 7, 6, 7, 8, 9, 9, 9, 8], 'Customer_Satisfaction': [70, 75, 80, 85, 88, 90, 95, 98, 100, 99] }

df = pd.DataFrame(data)
#print(df)

m = df.corr()
print(m)

sns.heatmap(m, annot=True)
plt.show()

unpacked = m.unstack()
highest = unpacked.idxmax()
#print(highest)

"""
FROM Heatmap and Corr Matrix Price and Quality with which  customers seems statisfied"""

