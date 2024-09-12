# appraoch one ; my approach
def first_second(my_list):
    # TODO
    num1 = -1
    num2 = -2
    for i in range(len(my_list)):
        if(my_list[i] > num1):
            num2 = num1 # save the old num1 to num2 before updating to new.
            num1 = my_list[i] # updating num1 one last time.
                
##########################################
# approach two : 2

def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
 
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
 
    return max1, max2
######################################################
# wrong Code below.               
"""
def first_second(my_list):
    # TODO
    num1 = -1
    num2 = -2
    for i in range(len(my_list)):
        if(my_list[i] > num1):
           num2 = num1
          num1 = my_list[i]
              
                   
       
    return (num1, num2)
#######################################################

"""
