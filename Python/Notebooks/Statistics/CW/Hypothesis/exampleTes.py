from scipy import stats
import math

mu_0 = 50
x_bar = 55
s = 10
n = 30
alpha = 0.05


t_stat = (x_bar - mu_0) / (s / math.sqrt(n))


df = n - 1
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))


print(f"t-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")


if p_value < alpha:
    print("Reject  null hypothesis ")
else:
    print("Fail to reject the null hypothesis")



