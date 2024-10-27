def positiveDiff(n1, n2):
    if n1>n2:
        diff=n1-n2
    else:
        diff = n2-n1
    return diff

res = positiveDiff(2,5)
print(res)
