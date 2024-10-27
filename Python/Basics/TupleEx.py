tuple1 = ()
print(type(tuple1))

nums = (1, 3, 4, 5, 7, 8, [2, 4, 5])

print("a" in nums)
print()
print(1 in nums)
print()
# print([2,4,5] in nums[6])
print("2 IN NUMS[6]",2 in nums[6])
print()
print("[2,4,5]== NUMS[6]", [2,4,5] == nums[6])

# built in cmp

T1 = [1,2,3,4]
T2 = [3,4,5]
if( (T1, T2) != 0):
    print("not same")
else:
    print("same")

print("max", max(T1))
print("mini ",min(T2))

T4 = ()
t4list = list(T4)
t4list.append("apple")
t4list.append("orange")
t4list.append("melon")
print(t4list)
back2tuple = tuple(t4list)
print(back2tuple)

a, *b = back2tuple
#temp = *b

#temp.append("muskmelon")
#*b = temp
print(a)
print(b)
print(type(b))


primes = [1,2,3,5,7,13,17,19]
print(primes[:-1])

