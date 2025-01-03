import matplotlib.pyplot as plt

data = {
         'Temperature': [25, 27, 22, 30, 28, 33, 35, 36, 34, 30],
         'Humidity': [60, 65, 55, 70, 75, 80, 85, 88, 90, 85],
         'Wind_Speed': [15, 10, 18, 12, 14, 20, 25, 22, 28, 18]
       }

import pandas as pd
import seaborn as sns

df = pd.DataFrame(data)


matrixx = df.corr()
print(matrixx)

sns.heatmap(matrixx, annot=True)
plt.show()

"""
From given data and correlation matrix, give most positive number for Humidty with temp.
as these shows Temperature varies more based on Humidity compare to other factors.
"""