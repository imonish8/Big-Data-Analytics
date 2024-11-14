def calculateRange(*args):
    min_ = min(args)
    maxi = max(args)
    range_ = abs(maxi - min_)

    print(f"\nMaximum : {maxi}, Minimum : {min_}, Range : {range_}")
    return min_, maxi,range_

calculateRange(1,2,3,4,5,6,7)
calculateRange(22,222,22222,222,1)


