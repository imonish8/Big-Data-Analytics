import numpy as np
from scipy import stats

fertilizer_A = [20, 22, 19, 18, 21]
fertilizer_B = [25, 24, 26, 27, 28]
fertilizer_C = [15, 17, 14, 16, 15]

F_stat, p_value = stats.f_oneway(fertilizer_A, fertilizer_B, fertilizer_C)


print(f"F-statistic: {F_stat}")
print(f"P-value: {p_value}")

null_h = 'There is no significant difference between the fertilizers.'
alt_h = 'There is a significant difference between the fertilizers.'

alpha = 0.05
if p_value < alpha:
    print(f"Reject the null hypothesis: {alt_h} ")
else:
    print(f"Fail to reject the null hypothesis: {null_h}")