import scipy.stats as stat
def customer(*args):
    max_ = max(args)
    min_ = min(args)
    range_ = abs(max_ - min_)
    IQR_ = stat.iqr(args)
    print(f"\nRange is : {range_}, Inter-Quartile-Range : {IQR_} {"Using Args"}")
    return range_, IQR_

def customerDATA(list):
    max_ = max(list)
    min_ = min(list)
    range_ = abs(max_ - min_)
    IQR_ = stat.iqr(list)
    print(f"\nRange is : {range_}, Inter-Quartile-Range : {IQR_} {"Using Provided Data"}")
    return range_, IQR_

data = [5, 6, 7, 8, 5, 9, 10, 6, 7, 8, 8, 6, 7, 5, 4, 9, 10, 10, 3, 2, 8, 7, 9, 5, 6]

customer(1,2,3,4,5)
customerDATA(data)