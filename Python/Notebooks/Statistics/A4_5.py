data_student = { 'Study_Hours': [2, 3, 4, 5, 6, 8, 10, 12, 14, 15], 'Grades': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95] }
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import seaborn as sns
df = pd.DataFrame(data_student)
print(df)
m = df.corr()
print(m)
"""
From corr, as it positive and close to 1 which means,
both values running in same direction,
As study hours increases, grades do increases.
"""
skew_ = round(stat.skew(df['Study_Hours']),2)
print("skewness of Study Hours : ",skew_)

skew__ = round(stat.skew(df['Grades']),5)
print("skewness of Grades : ",skew__)
mean__ = np.mean(df['Grades'])
# skewness for grades is zero, PERFECT SYMMENTRY
# aLL MEASURES OF CENTRAL TENDENCY WILL LIE IN CENTER FOR GRADES.
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Grades'], orient="h", color="skyblue")
plt.axvline(mean__, color='red')
#plt.axvline(mean_, color='red')
plt.xlabel("Student Grades")
plt.title("Grades distribution")
plt.show()
