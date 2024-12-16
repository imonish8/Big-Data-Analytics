import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dftrain = pd. read_csv('titanic/train.csv') # training data
print(dftrain.head())
deval = pd. read_csv('titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = deval. pop('survived')
print("Just Five rows of DataSet",dftrain.head())
print("Central Tendecy measures",dftrain.describe())
print("All Columns",dftrain.columns )
print("Shape",dftrain.shape)

sns.histplot(data=dftrain["age"],bins=20)
plt.show()

sns.barplot(data=dftrain["sex"].value_counts())
plt.show()

sns.barplot(data=dftrain['class'].value_counts())
plt.show()

(pd.concat ([dftrain, y_train], axis=1).groupby('sex').survived.mean()
 .plot(kind='barh').set_xlabel('% survive'))
plt.show()