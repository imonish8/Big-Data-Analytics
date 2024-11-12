import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data={'Advertising_exp':[500,600,700,800,900,1000,1100],
 'Product_price':[20,25,30,35,40,45,50],
 'Sales':[1000,1500,1600,1800,2200,2500,2700]}

df = pd.DataFrame(data)


mx = df.corr()
print(mx)
sns.heatmap(mx, annot=True)
plt.show()