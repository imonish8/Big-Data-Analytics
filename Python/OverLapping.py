def overLapping(var1, var2):
    for x in var1:
        for y in var2:
            if x == y:
                return True
                break
        return False
                
        


ListPrimes = list(filter(lambda x : x> 1 and all(x % i != 0 for i in range(2, int(x**0.5+1)+1)), range(1,50)))
ListEven = list(filter(lambda x : x>1 and all(x % 2 ==0 for i in range(2, 50)), range(1,50)))
ListOdd =  list(filter(lambda x : all(x % 2 != 0 for i in range(1,x)), range(1,50)))

"""
print("Primes")
print(ListPrimes)
print()
print("ListEven")
print(ListEven)
print()
print("ListOdd")
print(ListOdd)
"""
res = overLapping(ListPrimes, ListEven)
print(res)

print()
res1 = overLapping(ListPrimes, ListOdd)
print(res1)
