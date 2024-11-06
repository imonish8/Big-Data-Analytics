"""
1 < z < -1 68% values.
-2 < z < 2 95% values.
-3 < z < 3 99.7% values.

all are approx

Emperical Rule in-terms of Z SCORE.


FIVE NUMBER SUMMARY-

- quick way to summarise a data set using five key statistics that give insights into distribution of the data. it is often used as a precursive to further statistical analysis
thses five numbers help to describe the central tendency.

"""

import pandas as pd
from statistics import median


#data = list(map(int, input("Enter a list of numbers separated by commas: ").split(',')))
data = [70,85,90,95,60,78,88,72,80,92,85,74]

data_series = pd.Series(data)


minimum = data_series.min()
Q1 = data_series.quantile(0.25)
median_value = median(data)
Q3 = data_series.quantile(0.75)
maximum = data_series.max()


print("\nFive-Number Summary:")
print(f"Minimum: {minimum}")
print(f"Q1 (First Quartile): {Q1}")
print(f"Median (Q2): {median_value}")
print(f"Q3 (Third Quartile): {Q3}")
print(f"Maximum: {maximum}")

