import math
import scipy.stats as stat
null_h = 'There is significant difference exists'
alt_h = 'There is not much  significant difference exists'

sample_size_a = 15
sample_mean_a = 80
sample_std_dev_a = 5
sample_mean_b = 85
sample_size_b = 20
sample_std_dev_b = 6
# for this hypothesis, t-stat based on mean and combine_std_err
mean_diff = sample_mean_b - sample_mean_a
combine_std_err_sqrt = math.sqrt((sample_std_dev_a **2 / sample_size_a) + (sample_std_dev_b**2 / sample_size_b))

ind_sample_two_ttest = mean_diff / combine_std_err_sqrt
print(f"Independent Sample two t-test with WFH group and WFO found to be {ind_sample_two_ttest}")
df = sample_size_a + sample_size_b - 2

p_value = 2 * ( 1 - stat.t.cdf(ind_sample_two_ttest, df))
print(f'P value, evidence against Null Hypothesis is {p_value}')

alpha = 0.05
decision = None
if(p_value < alpha):
    decision = f'Reject the Hypothesis which says , {null_h} \nThis means there significantly difference in productivity of the employees.'
else:
    decision = f'Accept that {alt_h}, \nthis means there is no difference in productivity of the employess.'
print(decision)







