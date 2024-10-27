# creating tuple

# tuples are immutable and memory allocated is once defined 


# cannot change. which makes its complexity as low as O(1).


newTuple = (1,2,3,4,5)

print(newTuple)

newTuple1 = ('a',)

print(newTuple1)

newTuple3 = tuple('abcede')

print(newTuple3)

print("\nSliced tuple down")
print(newTuple[2:4])


# traverse loop
# Tuple traverse O(N)
# "in" operator works one by one so time complexity will be 1.


print("Traverse in tuple")
for val in newTuple:
	print(val)

print('a' in newTuple)

print(newTuple3.index('e'))

def searchTuple(p_tuple,element):
	for i in range(0, len(p_tuple)):
		if p_tuple[i] == element:
			return f"The {element} is not Found at{i} index"
	return 'The Element is not found.'

print(searchTuple(newTuple, 'b'))

# count returns the count of given element in tuple.
print(newTuple.count(2))

# max/min function returns max/mini element in terms of numbers.
print(max(newTuple))
print(min(newTuple))

del newTuple3
# del not just emppty the tuple it deletes entire def

# print(newTuple3)

#tuple in list

list1 = [(1,2),(2,4),(3,4)]
print(list1)

# list inside tuple

tuple5 = ([],[22,4],[44,44])
print(tuple5)


"""
Creating tuple take O(1) time complexity.
creating tuple take O(N) space complexity.

traversing take O(N) runtime.
space takes O(1)

accessing takes O(1)
space takes O(1)

searching takes O(N)
space takes O(1).
"""
