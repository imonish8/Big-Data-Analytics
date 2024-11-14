
import scipy.stats as stat
import pandas as pd

def usingPythonLibrary(list):
    df = pd.DataFrame({'data' : list})
    mean_ = df['data'].mean()
    median_ = df['data'].median()
    IQR_ = stat.iqr(df['data'])
    skew_ = stat.skew(df['data'])
    if(skew_ < 0):
        print(f"outliers are extending to left and mean is less than median"
              f"\nMean : {mean_}, Median : {median_}, IQR : {IQR_}")
    elif(skew_ >0):
        print("Outliers are extending to right and mean is greater than median"
              f"\nMean : {mean_}, Median : {median_}, IQR : {IQR_}")
    else:
        print("The Distribution of House price is Perfect symmetry,"
              "\nAll central tendency Measure lie on the same central line."
              f"\nMean : {mean_}, Median : {median_}, IQR : {IQR_}")
    return mean_, median_, IQR_

Dataset =[150000, 175000, 200000, 220000, 230000, 250000, 270000, 300000, 320000,340000, 350000, 375000, 400000, 425000, 450000, 500000, 600000, 750000, 900000, 1000000]
usingPythonLibrary(Dataset)
