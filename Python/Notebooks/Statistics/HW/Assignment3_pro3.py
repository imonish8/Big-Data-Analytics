#mean #median #iqr
import pandas as pd

import numpy as np
house_prices = [150000, 175000, 200000, 220000, 230000, 250000, 270000, 300000, 320000,
340000, 350000, 375000, 400000, 425000, 450000, 500000, 600000, 750000, 900000, 1000000
]
df = pd.Series(house_prices)


def centralTendency(data):
    df = pd.Series(data)
    mean_value = sum(data) /  len(data)
    median_val = np.percentile(data, 50)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    print(f"Mean Value : {mean_value} \nMedian Value : {median_val} \nInter-Quartile-Range : {iqr}")
    return mean_value, median_val, iqr

centralTendency(house_prices)
