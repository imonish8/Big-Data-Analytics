def printFactors(n):
    for i in range(1,n+1):
        if(n % i == 0):
            print("Factors are ",i)

printFactors(22)



def usingWHILE(w):
    i = w
    while(i >0):
        if(w%i==0):
            print(f"factor of {w} is :", i)
        i = i -1

usingWHILE(33)
