def sumOfN(n):
    adding  = 0
    if(n==1):
        adding =1
    else:
        for i in range(1, n):
            adding = i + adding
        return adding
    return adding


res1 = sumOfN(1)
print(res1)
res2 = sumOfN(11)
print(res2)
