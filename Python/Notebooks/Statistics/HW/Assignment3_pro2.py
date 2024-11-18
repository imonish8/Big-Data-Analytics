import numpy as np

dataSet = [5, 6, 7, 8, 5, 9, 10, 6, 7, 8, 8, 6, 7, 5, 4, 9, 10, 10, 3, 2, 8, 7, 9, 5, 6]

def cal_IQR(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    print(f"Q1 : {q1} \nQ3 : {q3} \nInter-Quartile-Range : {iqr}")
    return q1, q3, iqr

cal_IQR(dataSet)
