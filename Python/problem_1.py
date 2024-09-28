def missing_number(arr, n):
    # TODO
    sum_natural = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    missing_number = sum_natural - actual_sum
    
    return missing_number
    
        
        
        
        
        
        
        
        
        
    
    """
    
    brute force approach
    arr = [1,2,3,4,5,6,8,9]
    perfect_list = [1,2,3,4,5,6,7,8,9]
    miss_num = array.array('i',[])
    
    
    for i in range(0,n):
            if(arr[i] != perfect_array[i]):
                miss_num.extend(perfect_array[i]):
    
    other Approach :
    sum - actual_sum = missing number.
                
                
            
    
    unknown_missing_value = -1
    
        
    """
