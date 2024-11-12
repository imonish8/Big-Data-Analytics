import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import skew

data = [ 30, 45, 35, 50, 60, 55, 40, 42, 58, 65, 70, 55, 50, 45, 48, 72, 68, 30, 75, 78, 85, 80, 95, 90, 100, 50, 55, 45, 70, 75, 150, 200, 180, 25, 40, 45, 35, 50, 52, 60, 65, 30, 70, 85, 95, 80,100, 10, 60, 110, 10, 40]


plt.figure(figsize=(10, 6))
sns.boxplot(data=data, orient="h", color="skyblue")
plt.xlabel("Workout Duration (minutes)")
plt.title("Boxplot of Workout Durations at the Fitness Center")
plt.show()

data_series = pd.Series(data)
Q1 = data_series.quantile(0.25)
Q3 = data_series.quantile(0.75)
IQR = Q3 - Q1

#out
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


outliers = data_series[(data_series < lower_bound) | (data_series > upper_bound)]
print(f"Outliers:\n{outliers.tolist()}")

#skew
data_skewness = skew(data)
print(f"\nSkewness of workout durations: {data_skewness:.2f}")

average_time = np.average(data)
print(round(average_time, 2))
if data_skewness > 0:
    print("data is positively  working out, with a few spending much longer.")
elif data_skewness < 0:
    print("data is negatively skewed  working out, with a more spending much longer.")
else:
    print("data is symmetric, around the average workout time.")