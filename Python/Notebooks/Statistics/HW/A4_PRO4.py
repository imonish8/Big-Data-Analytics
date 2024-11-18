data = { 'Income': [45000, 54000, 60000, 63000, 70000, 75000, 80000, 100000, 120000, 150000] }

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
import seaborn as sns

df = pd.DataFrame(data)
print(df)

skew_ = skew(df)
print(skew_)

mean_ = np.mean(df)


# skewness is positive
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, orient="h", color="skyblue")
plt.axvline(mean_, color='red')
plt.xlabel("Income")
plt.title("Income Distribution")
plt.show()

"""
From Box plot, concluding Mean is moving towards the outliners which at right side which
skewness is also positive implies right side mean should lie to median.

"""