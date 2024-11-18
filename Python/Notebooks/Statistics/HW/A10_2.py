import scipy.stats as stat



online = [10, 20, 34, 33, 45 ,67,64,78,99,77 ]
offline = [10, 30, 44, 44, 46 ,50,32,69,60,77 ]
hybrid = [33, 45, 33, 66, 69 ,72,78,80,99,94 ]

groups = [online, offline, hybrid]
f_stat, p_val = stat.f_oneway(*groups)
alpha = 0.05
if p_val > alpha:
    decision = '\nAccept the Null Hypothesis, No Significant Difference between the groups. '
else :
    decision = ('\nReject the null hyoothesis which means '
                '\nAtleast one group Mean is significantly different.')

print(decision)
print(f"\nP value is : {p_val}")
print(f'\n if P values is 0.03, this would imply a strong evidence against null Hypothesis'
      f'\nWe would reject Hypothesis at p = 0.03 with risk of 5% i.e 0.05')
