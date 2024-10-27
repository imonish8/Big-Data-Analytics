digits = [1,2]
nums = ["One", "Two"]

#using dict zip

newDict = dict(zip(digits, nums))
print(newDict)


print()
print("Taking input from user")
print()
print()

n = int(input("Enter the number of key-value pair"))

marks = {}
for _ in range(n):
	key = input("Enter key ")
	value = input("Enter value for {key}")
	marks[key] = value
	
print("Resulting dictionary of key value pair is :   ", marks)
