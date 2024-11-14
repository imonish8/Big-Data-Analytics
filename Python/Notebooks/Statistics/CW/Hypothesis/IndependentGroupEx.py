
from scipy.stats import ttest_ind

groupA = [ 12, 15, 14, 10, 13, 15, 16]
groupB = [14,16, 13, 18, 19, 17, 16, 18]

na = 20
nb =  25
test, p = ttest_ind(groupA, groupB)


""""""

import math
from scipy import stats


meanA = 78
stdA = 5
nA = 20

meanB = 82
stdB = 6
nB = 25

numerator = meanA - meanB
denominator = math.sqrt((stdA**2 / nA) + (stdB**2 / nB))
t_stat = numerator / denominator


#df = ((stdA**2 / nA + stdB**2 / nB)**2) / ((stdA**2 / nA)**2 / (nA - 1) + (stdB**2 / nB)**2 / (nB - 1))
df = nA + nB - 2
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))


print(f"t-statistic: {t_stat:.4f}")
print(f"Degrees of freedom: {df:.4f}")
print(f"P-value: {p_value:.4f}")


alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in mean scores between Group A and Group B.")
else:
    print("Fail to reject the null hypothesis: No significant difference in mean scores between Group A and Group B.")