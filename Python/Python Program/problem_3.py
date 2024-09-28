def middle(lst):
    # TODO
    new_list = []
    for i in range(1,len(lst)-1):
        new_list.append(lst[i])
    return new_list
        
# time Complexity : O(n)
# space : O(n)

# Brute force approch 
def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]
 
my_list = [1, 2, 3, 4]
 
print(middle(my_list))  # Output: [2, 3]

# time : O(1)
# spce : O(1)
