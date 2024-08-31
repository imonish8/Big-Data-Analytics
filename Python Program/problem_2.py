# max product

# My Approach :
def product(a, b):
    return a * b

def max_product(arr):
    max_product = -1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # Start j from i+1 to avoid repetition and self-multiplication
            current_product = product(arr[i], arr[j])
            if max_product < current_product:
                max_product = current_product
    return max_product
# Time Complexity : O(N^2)
# Space Complexity : O(1) since the method product will always diappear instantly in call stack of the memory.

# secondary Appraoch :

def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
 
    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
 
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication

# Time Com : O(N)
# space : O(1)
