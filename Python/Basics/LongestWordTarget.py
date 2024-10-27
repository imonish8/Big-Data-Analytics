#Approach 1 O(1)
"""
def LongestWordTarget(*args, n):
    if not args:
        return None
    else:
        longest = max(args, key=len)
        leng = len(longest)
        if(leng == n):
            pr = "TARGET MATCHED"
    return str(longest)+" "+str(leng)+pr

output = LongestWordTarget(("Hello", "World", "I","lOVE","pYTHON"),6)
print(output)
"""
#approach2 O(n)
#def LongestWordTarget(
def LongestWordTargetLoop(list1, n):
    long = list1[0]
    longLen = len(list1[0])
    flag = False

    if not list1:
        return None
    else:
        for i in range(1, len(list1)):
            if(len(long) < len(list1[i])):
               long = list1[i]
               longLen = len(long)
            if(longLen == n):
                       flag = True
               
        return str(long)+" "+str(longLen)+" "+str(flag)

res = LongestWordTargetLoop(["Avocado", "Dragon","Starwberries","BlackBerries","Green Apple"], 4)
print(res)
