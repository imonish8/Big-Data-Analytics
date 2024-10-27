import pandas as pd

list1 = [2,5,6,8,10,12]
list2 = [4,3,6,5,8,7]

sorted_list = sorted(list1)
reverse_sorted = sorted(list2, reverse=True)

paired_list = list(zip(sorted_list, reverse_sorted))

df = pd.DataFrame(paired_list, columns=['List1', 'List2'])

print(df)
