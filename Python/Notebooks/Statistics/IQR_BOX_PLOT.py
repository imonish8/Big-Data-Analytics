import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = [45,47,52, 54, 58, 60, 63, 62, 71, 72, 75, 76, 81, 82, 85, 89, 92, 96, 555, 50, 888, 90]
print(data)

plt.figure(figsize=(8,6))
sns.boxplot(data, orient="h")
plt.title('Box Plot')
plt.show()