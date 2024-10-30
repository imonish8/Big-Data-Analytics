import pandas as pd

df = pd.read_csv("Life Expectancy Data.csv")

"""
headers = df.head()
print(headers)
print(df)

col = df.columns
print(col) #list of cols.

plts = df.plot
print(plts)

desc = df.describe()
print(desc) #table of stats.

#desc_ops = df.describe_option

print("info >>>>>>>>>>>>>>.")
print("INFO",df.info)

print("Nulls >>>>>>>>>>>>>>>.")
nulvals = df.isnull().sum()
print(nulvals)

print(df.describe(include='all'))

print(df.isnull().sum())

# col manipulation
df.rename
"""

df.boxplot(column='Year')
