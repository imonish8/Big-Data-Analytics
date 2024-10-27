import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('earthquakes_2023_global.csv')

head_records = df.head()

print(head_records)

#print(df)

df['time'] = pd.to_datetime(df['time'])

df['Year'] = df['time'].dt.year
df['Month'] = df['time'].dt.month
df['time'] = df['time'].dt.day

df = df.dropna(subset=['mag', 'depth', 'latitude', 'longitude'])

def categorize_magnitude(mag):
    if mag < 2.0:
        return "Micro"
    elif 2.0 <= mag < 4.0:
        return "Minor"
    elif 4.0 <= mag < 6.0:
        return 'Light'
    elif 6.0 <= mag < 7.0:
        return "Strong"
    elif 7.0 <= mag < 8.0:
        return "Great"

# in apply method can pass function as arguments to apply for a column.
df['Magnitude_Type'] = df['mag'].apply(categorize_magnitude)
print('\ndf.describe >>>>>>')
print(df.describe())

#basially the correlation between two columns tells us via pattern or something...
# if the number is 1 perfectly correlated the pattern, -1 bad correlation and 0 no correlation.

#positive is good, negative corr means bad.
corr_matrix = df[['mag', 'depth']].corr()
print(corr_matrix)

eq_per_year = df['time'].value_counts().sort_index()
print('\neq_per_year')
print(eq_per_year)


plt.figure(figsize=(12,6))
plt.plot(eq_per_year.index, eq_per_year.values, marker='o')
plt.title("Earthquackes per Year Viz")
plt.xlabel("Year")
plt.ylabel("No of Eartquacks")
plt.grid(True)
plt.show()

#plt.legend()

print("\nSeaborn Statistical Data is applied to continuous values Distribution ")
plt.figure(figsize=(10,6))
sns.histplot(df['mag'], bins=100, kde=True)
plt.title('Distribution of Earthquack Magnitudes ')
plt.xlabel("Magnitude")
plt.ylabel('Frequency')
plt.show()


# depth vs magnitude.
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'depth', y = 'mag', data=df)
plt.title("Depth vs. Magnitude")
plt.xlabel("Depth")
plt.ylabel("Magnitude")
plt.show()


#histo better at freq than scatter.

plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot = True, cmap = 'coolwarm')
plt.title("Correlation matrix")
plt.show()




