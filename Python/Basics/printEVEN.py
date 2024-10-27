def printEven(n):
    for i in range(1, n):
        if(i % 2 == 0):
            print(i, " ")

printEven(50)

EVENnums = list(filter(lambda x : x % 2 ==0, range(1,50)))
print()
print(EVENnums)
