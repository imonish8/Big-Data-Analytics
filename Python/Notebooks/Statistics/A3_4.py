import scipy.stats as stat
import pandas as pd
import numpy as np

def BMI(list):
    df = pd.DataFrame({"BMI" : list})
    min_ = np.min(df)
    max_ = np.max(df)
    range_ = abs(max_ - min_)
    IQR = stat.iqr(df)
    std_ = np.std(df)
    print(f"\nRange : {range_}"
          f"\nIQR : {IQR}"
          f"\nStdandard Deviation : {std_}")
    return range_, std_, IQR

Dataset= [18.5, 19.0, 20.2, 21.5, 22.0, 23.5, 24.0, 25.5, 26.0, 27.0, 28.5, 29.0, 30.5, 31.0,
32.5, 33.0, 34.0, 35.5, 36.0, 37.5, 40.0]

BMI(Dataset)