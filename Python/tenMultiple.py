def tenMultiple(n,n1):
    for i in range(1,n1):
        print(i*10," ")


tenMultiple(10,20)
print()
print()

multTEN = list(map(lambda x : x*100, range(1, 20)))
print(multTEN)
