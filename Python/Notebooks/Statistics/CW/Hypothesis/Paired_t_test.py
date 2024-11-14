"""
Paired t-test compares the means of two related groups, to determine if there is a statistically
significant difference, between them, the main feature of the test is that, is obervation in one
group, is paired with, a related observation in the other groups.

the paired t-test is typically used when the two groups are dependent on the related.
examples,
 1. before and after studies.
    comparing measurements taken before and after a treatment, on the same subjects,
 2. Matched pairs measuring the effect of training program of the employees, by comparing
 their performance score, DEPENDINF ON THIER PEROFRMANCE


DEPENDENCE OF OBERVATION IN ONE GROUP, MUST HAVE A RELATED, OR MATCHED OBSERVATION.
IN THE OTHER GROUP.

SECOND ASSUMPTION NORMALITY OF DIFFERENCES, THE DIFFERENCES BETWEEN PAIRED OBSERVATIONS,
SHOULD FOLLOW A NORMAL DISTRIBUTION. ESPECIIALY FOR SMALL SAMPLE SIZES.
"""

from scipy.stats import ttest_rel
before = [20, 22, 21, 23, 24, 20, 19]
after = [23, 224, 27, 22, 29, 27, 21]

test, p = ttest_rel(before, after)

a = 0.05
if(p  >= a):
    print("accept")
else:
    print('reject')

from scipy import stats
import math

mu_0 = 3
x_bar = 3.5
s = 1.2
n = 50
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

