#approach1 O(N)
def filter_longWord(list1, n):
    filter_list =[]
    for i in range(1, len(list1)):
        if((len(list1[i]) >= n)):
            filter_list.append(list1[i])
    return filter_list

res = filter_longWord(["Hello", "World", "Python", "Anaconda"], 5)
print(res)


#approach2
listForLambda = ["Hello", "World", "Python", "Anaconda"]

filtered = list(filter(lambda x : len(x) > 5, listForLambda))
res1 = filtered
print(res1)
