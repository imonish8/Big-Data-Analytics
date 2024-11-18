import numpy as np
import matplotlib.pyplot as plt

data = [12, 15, 14, 10, 8, 15, 14, 12, 11, 16, 30]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower= Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = [x for x in data if x < lower or x > upper]

if outliers:
    print(f"The outliers are {outliers}. These outliers can skew the mean and affect the analysis of the dataset.")
else:
    print("There are no outliers in the dataset.")

print(f"Lower Bound: {lower}")
print(f"Upper Bound: {upper}")
print(f"Outliers: {outliers}")

plt.boxplot(data)
plt.title("Boxplot for Dataset")
plt.ylabel("Values")
plt.show()
