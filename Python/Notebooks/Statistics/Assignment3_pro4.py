import numpy as np

def show_stats(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    std_deviations = round(np.std(data), 2)
    min_val = np.min(data)
    max_val = np.max(data)
    range_ = max_val - min_val

    print(f"Range of the DataSET is {range_} \nInter-Quartile-Range : {iqr}  \nStandard Deviation : {std_deviations}")

BMI = [18.5, 19.0, 20.2, 21.5, 22.0, 23.5, 24.0, 25.5, 26.0, 27.0, 28.5, 29.0, 30.5, 31.0,
32.5, 33.0, 34.0, 35.5, 36.0, 37.5, 40.0
]
show_stats(BMI)