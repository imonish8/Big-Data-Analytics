list1 = [11,222,3343,5433,322]
print(list1)

#append
list1.append("Goa")

# insert
list1.insert(3, 54.90)
print(list1)

#remove
list1.remove("Goa")
print(list1)

# pop
list1.pop(2)
print(list1)

# del
del list1[0]
print(list1)

# slicing
fruits = ["Apple", "Pineapple", "Melon"]
print(fruits[:3])

# negative slicing will start from end
# positive slicing will start from 0th index

print(fruits[-1:-2])
