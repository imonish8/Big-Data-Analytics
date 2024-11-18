from collections import Counter
import numpy as np
data = [22, 25, 20, 18, 30, 28, 24, 27, 26, 19, 21, 29]
mean = np.mean(data)
median = np.median(data)

counted_data = Counter(data)
mode_ = counted_data.most_common(1)[0][0]

Q1 = np.percentile(data, 25)
Q2 = median
Q3 = np.percentile(data, 75)

print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Mode: {mode_}")
print(f"First Quartile (Q1): {Q1}")
print(f"Second Quartile (Q2/Median): {Q2}")
print(f"Third Quartile (Q3): {Q3}")

spread = round(Q3 - Q1,2)
print(f"\nSpread OF (IQR = Q3 - Q1): {spread}")

if spread < 10:
    print("Data is compact not much spread.")
elif spread < 20:
    print("Less Wide Distributiion.")
else:
    print("Wide Spread Distribution.")