import matplotlib.pyplot as plt
import numpy as np


data_rating = { 'Ratings': [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5] }

import pandas as pd
import seaborn as sns
import scipy.stats as stat

df = pd.DataFrame(data_rating)

mean_ = np.mean(df)
skew_ = round(stat.skew(df['Ratings']),2)
print(f"Skewness of rating is : {skew_}")

"""
Skewness is negative which means the the tail is long at left implies mean is moving towards
the outliers which mostly reside in left mean is less than median. Mode is largest of all here.

As boxplot shows mean moving towards the outliers tail in left and 
median is towards the most values which resides towards right.

"""

sns.boxplot(data=df, orient='h', color='green')
plt.xlabel("Ratings")
plt.title("Box plot for Rating distribution")
plt.axvline(mean_, color='red')
plt.show()