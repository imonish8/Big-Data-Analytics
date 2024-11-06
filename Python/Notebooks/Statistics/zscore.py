import pandas as pd
from statistics import mean, stdev


sales_data = [500, 450, 520 ,580,600 ,620 ,700, 750, 800 ,850, 900, 950]


mean_sales = mean(sales_data)
std_dev_sales = stdev(sales_data)


df = pd.DataFrame(sales_data, columns=['Sales'])
df['Z-score'] = (df['Sales'] - mean_sales) / std_dev_sales


df['Abnormal_sales'] = df['Z-score'].apply(lambda z: 'Yes' if abs(z) > 2 else 'No')


print("Mean Sales:", mean_sales)
print("Standard Deviation of Sales:", std_dev_sales)
print("\nMonthly Sales Analysis:")
print('abnormal :', df['Abnormal_sales'])
print(df)