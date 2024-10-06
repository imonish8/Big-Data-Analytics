def maxLIST(var):
    l = len(var)

    maxNUM = var[0]
    
    for i in range(1, l):
        if(var[i] > maxNUM):
            maxNUM = var[i]
    print(maxNUM)

maxLIST([2,3,4,5,7,99999,2])
