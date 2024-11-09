PYTHONWARNINGS="ignore"
import matplotlib.pyplot as plt
import pandas as pd

data={'size':[1500,1800,2400,3000,3500,4000,4500,5000,5500,6000],
'bedrooms':[3,4,3,5,4,5,6,7,6,8],
'age':[10,15,8,20,25,30,35,40,50,60],
'price':[400,450,500,600,650,700,750,800,850,900]}

df = pd.DataFrame(data)

priceSize = df['price'].corr(df['size'])
print(f"Price vs Size {priceSize}")
priceBedrooms = df['price'].corr(df['bedrooms'])
print(f"Price Vs Bedroom {priceBedrooms}")
priceAge = df['price'].corr(df['age'])
print(f"price vs Age : {priceAge}")

# All factors positive corr with Price
# Most influential one is Size

print('\ncorr matrix')
matrixx = df.corr()

unpack_matrixx = matrixx.unstack()
#high, highv = max(matrixx).idxmax()
highest_corr_pair = unpack_matrixx.idxmax()
print(f"Hihest :  {highest_corr_pair}")

"""
import seaborn as sns
sns.heatmap(matrixx, annot=True)
plt.show()

"""