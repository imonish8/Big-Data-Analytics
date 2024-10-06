#hybrid apporach
# O(n)
def _longest_word(*args):
    for word in args:
        if not  args:
            return 0
        else:
            longWord = max(args, key=len)
            
    return longWord

res = _longest_word("Apple", "Banana","Pineapple")
print(res)
print()

#####################
# most optimistic approach O(1)
def longestWord(list1):
        return max(list1, key=len)

print()
res1 = longestWord(["Banana", "Apple", "Watermelon"])
print(res1)



######################
#brute force approach O(n)
def LongestWord(list1):
    if not list1:
        return None

    long = list1[0]
    
    for i in range(1, len(list1)):
        if(len(long) < len(list1[i])):
            long = list1[i]
    return long

print()
res2 = LongestWord(["lemon","Cucumber","carrot","beetroot"])
print(res2)
#######################
