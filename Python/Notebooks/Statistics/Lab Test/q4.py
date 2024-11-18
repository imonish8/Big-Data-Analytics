import numpy as np
from scipy import stats

method_A = np.array([82, 88, 84, 86, 90, 85])
method_B = np.array([78, 80, 83, 79, 81, 77])

mean_A = np.mean(method_A)
mean_B = np.mean(method_B)
std_A = np.std(method_A, ddof=1)
std_B = np.std(method_B, ddof=1)
n_A = len(method_A)
n_B = len(method_B)

t_stat, p_value = stats.ttest_ind(method_A, method_B)

alpha = 0.05

null_h = 'There is NO significant difference between the two methods.'
alt_h = 'There is a significant difference between the two methods.'

if p_value < alpha:
    print(f"Reject the null hypothesis: {alt_h} ")
else:
    print(f"Fail to reject the null hypothesis: {null_h}")

print(f"T-STATISTICS: {t_stat:.2f}")
print(f"P-VALUE: {p_value:.4f}")
