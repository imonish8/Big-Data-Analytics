"""Alternate way"""
#numbers = list(map(int, input("Enter a list of numbers separated by commas: ").split(',')))
max_num = 0
min_num = 0

def cal_range(*args):
    max_num = max(args)
    min_num = min(args)
    range_  = max_num - min_num

    print(f"Maximum : {max_num}, \nMinimum : {min_num}, \nRange Of Dataset : {range_}")
    return max_num, min_num, range_

cal_range(1, 2, 3, 4, 5,10)



