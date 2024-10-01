import copy as cp

l1 = [222,2423,2322,111,555]
l3 = cp.deepcopy(l1);
print(l3)
print(id(l1))
print(id(l3))
l1 = ["eeee","eeee"",@@@"]
print(id(l3))
