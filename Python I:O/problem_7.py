# pair sum
def pair_sum(myList, sum):
    # TODO
    # num1 = sum - num2
    pairs = []
    
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if(sum == myList[i]+ myList[j]):
                pairs.append((str(myList[i]))+'+'+str((myList[j])))
        
    
    return pairs
  
