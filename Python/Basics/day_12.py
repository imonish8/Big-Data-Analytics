my_dict = {
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven"
}

my_dict2 = {
	0 : "Zero",
	False: "False"
}

# 'in' opertor works with keys not with values

# 'not in' operator too works with keys NOT WITH VALUES.

print("ten" in my_dict.values())

print("ten" not in my_dict.values())
print(len(my_dict))

print(all(my_dict))

# all() will return true only if ALL true
# returns false if any key false.
print(all(my_dict2))

# sorted() will return list of keys for dict
print(sorted(my_dict))

# List are ordered and Dict are unordered.
# access via index , key
# unique key values.
# ordered data.
# no duplicate in dictionary , list had unique values/

# searching or creating takes O(N) time complexity.

# Dict Comprehsion

new_dict = {new_key:new_value for (key,value) in dict.items() cond}
