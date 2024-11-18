import scipy.stats as stat
NULL_H = 'FIBER CONSUPTION IS 30gm'
alt_h = 'Fiber consumption is not 30gm'

sampel_size = 25
sample_mean = 28
pop_mean = 30 #claimed for populatipon overall
sample_STD  = 4
alpha = 0.05
mean_diff = sample_mean - pop_mean
sample_std_err = sample_STD / sampel_size ** 0.5

t_score = mean_diff / sample_std_err

df = sampel_size - 1
#this is a two tailed test (t_critical = stat.t.ppf(1 - risk / 2), df)

p_value = 2 * ( 1 - stat.t.cdf(t_score, df))
critical = 1.96
if(p_value < alpha):
    print(f"\nWe reject the Null Hypothesis, {alt_h}")
else:
    print(f"\nWe failed to reject the null hypothesis that, {NULL_H}")
