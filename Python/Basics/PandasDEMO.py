# /Users/imonish8/Desktop/Big-Data-Analytics/PycharmProjects/MortalityFactors/Life Expectancy Data.csv
from unittest.mock import inplace

import pandas as pd

data = pd.read_csv('/Users/imonish8/Desktop/Big-Data-Analytics/PycharmProjects/MortalityFactors/Life Expectancy Data.csv')

#exploration.
print(data.info())
desc = data.describe()
print(desc)
descall = data.describe(include='all')
print(descall)
nulltotal = data.isnull().sum()
print(nulltotal)

#column and data manipulation
data.rename(columns = {'Polio' : 'PolioCount'}, inplace=True)
data.drop(columns = ['Alcohol'], inplace=True)
#data.['Column_name'].replace({old_value : new_value}, inplace=True)
data['Life Expectancy'].fillna(data['Life Expectancy'].mean(), inplace=True)

#data cleaning
data.drop_duplicates(inplace=True)
data['Column_name'] = data['Column_name'].astype('new dtype')
data.boxplot(column = 'Year')

#Data Grouping
# Grouping data and calculating mean
data.groupby('Country').mean()
# Multiple aggregations
data.groupby('Country').agg({'Life expectancy': ['mean', 'min', 'max']})
# Pivot table example
data.pivot_table(values='Life expectancy', index='Country', columns='Year', aggfunc='mean')

#Indexing Sorting
# Setting an index
data.set_index('Column_Name', inplace=True)
# Sorting values
data.sort_values(by='Life expectancy', ascending=False)
# Multi-indexing
data.set_index(['Country', 'Year'], inplace=True)

# Handling Missing Data.
# Dropping rows with null values
data.dropna(inplace=True)
# Forward or backward filling of missing data
data.fillna(method='ffill', inplace=True)

#Data Merging Concating
# Merging datasets
merged_data = pd.merge(data1, data2, on='Common_Column')
# Concatenating datasets
concatenated_data = pd.concat([data1, data2], axis=0)

#Feature Engineering
# Creating new columns
data['New_Column'] = data['Column1'] + data['Column2']
# Applying functions
data['Column_Name'] = data['Column_Name'].apply(lambda x: x + 10)
# Binning continuous data
data['Life_Category'] = pd.cut(data['Life expectancy'], bins=[0, 50, 70, 100], labels=['Low', 'Medium', 'High'])

#Dates
# Converting to datetime
data['date_column'] = pd.to_datetime(data['date_column'])
# Extracting year and month
data['Year'] = data['date_column'].dt.year
data['Month'] = data['date_column'].dt.month

#with matplot.pyplot
import matplotlib.pyplot as plt
# Basic histogram plot
data['Life expectancy'].plot(kind='hist')
plt.show()
# Scatter plot
data.plot(kind='scatter', x='GDP', y='Life expectancy')
plt.show()
# Boxplot
data.boxplot(column='Life expectancy', by='Country')
plt.show()

# Exporting to new file or renaming
# Saving data to a new CSV file
data.to_csv('processed_life_expectancy_data.csv', index=False)