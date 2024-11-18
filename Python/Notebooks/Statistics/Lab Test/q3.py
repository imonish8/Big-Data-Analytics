import numpy as np
from scipy import stats
data = np.array([162, 167, 160, 163, 170, 168, 166, 164, 159, 161])

mu_0 = 165
alpha = 0.05
size = len(data)

sample_mean = np.mean(data)
sample_std = np.std(data)
sample_std_err = sample_std / np.sqrt(size)
mean_diff = sample_mean - mu_0

t_stat = mean_diff / sample_std_err

df = size - 1

p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Standard Deviation: {sample_std:.2f}")
print(f"T-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")

null_h = 'The average height of the employees is 165 cm.'
alt_h = 'The average height of the employees is NOT 165 cm. (TT)'
if p_value < alpha:
    print(f"Reject the null hypothesis: which mean alt hypo is true {alt_h}")
else:
    print(f"Fail to reject the null hypothesis: which says that, {null_h}")