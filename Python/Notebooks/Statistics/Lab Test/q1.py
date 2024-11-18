import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter
data = [12, 15, 14, 10, 8, 15, 14, 12, 11, 16]
mean_ = np.mean(data)
median_ = np.median(data)
counted_data = Counter(data)
mode_ = counted_data.most_common(1)[0][0] 

std_dev = np.std(data)

print(f"Mean: {mean_}")
print(f"Median: {median_}")
print(f"Mode: {mode_}")
print(f"Standard Deviation: {std_dev}")

plt.hist(data, bins=6, edgecolor='black', alpha=0.7)
plt.title('Histogram Plot')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()