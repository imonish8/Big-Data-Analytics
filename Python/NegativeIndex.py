# list[start : stop : step]
# Slicing means slicing it not reversing or anything.

mylist = [10, 20, 30, 40, 50, 60, 70]

print(mylist)

print(mylist[-7:]) # -7 to zero, prints from 
print("0 to -5"+str(mylist[:-5])) #mylist[0 : -5])

print("[-5:-2]" +str(mylist[-5:-2]))
print("[-5:-3]" +str(mylist[-5:-3]))

# count

print(mylist.count(30))
#print(reverse(mylist))

# reverse

wo = ["hello", "owl", "ool"]
wo.reverse()
print(wo)
print("reverse", wo)

# sort(reverse=true/false)

jungle = ["tree", "deer", "panther"]
jungle.sort(reverse=True)
print(jungle)

l2 = [23, 34, 56, 66]
print(l2[::-1])

#clear

print(l2.clear())
#del wo
#print(wo)

# nest list
list1 = [2,3,4,[33,332,23],33]
list1[3][2] = 444
print(list1)

#length
list_len = [2,4,5,2,4,3]
print(len(list_len))

# sort by length
sortlen = [[2222,22222],[22]]
sortlen.sort(key=len)
print(sortlen)


#copy
nonon = [222,333,33333,3333333,32]
print(id(nonon))
onon = nonon.copy()

# pppp = onon
pppp = onon
print(onon)
print(id(onon))
print(pppp)
print(id(pppp))


# membership
# in not in
Zoo = ["Lion", "Zebra", "Cheetah"]
a = "Lion" in Zoo
print(a)
print(type(a))
b = "Tiger" not in Zoo
print(b)
print(type(Zoo))

# Max min sum

campus = ["Stud", ["Teacher"," Professors"],["Lab", "Assistance"]]

# print("Max", max(len(campus)))

Nums = [11,21,22,212,211]
Nums2 = [22,11,45,29]
for x in Nums:
    for y in Nums2:
        if(x == y):
            print(x)

L3 = ['A', 'E', '4', '3333' , [20, 30, 50], (3,4,6)]

print(L3[-1][-2:-1])
print(L3[-3][3])
print(L3[-1][-2])

    
                    

#list *= n



