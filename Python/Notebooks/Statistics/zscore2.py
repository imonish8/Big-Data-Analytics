import pandas as pd
from statistics import mean, stdev, variance


salaries = [45000, 50000, 55000, 48000, 53000, 52000, 50000, 57000, 58000, 60000]


variance_salaries = round(variance(salaries), 2)

print(f"Variance of salaries: {variance_salaries}")


mean_salary = mean(salaries)
std_dev_salary = stdev(salaries)


df = pd.DataFrame(salaries, columns=['Salary'])
df['Z-score'] = (df['Salary'] - mean_salary) / std_dev_salary


df['Unusual'] = df['Z-score'].apply(lambda z: 'Yes' if abs(z) > 0 else 'No')
df['aboveMean'] = df['Z-score'].apply(lambda z: 'Yes' if z > 0 else 'No')

print("\nEmployee Salary Analysis:")
print(df)

