import scipy.stats as stat
sample_mean = 26
sample_size = 60
sample_std = 6
pop_mean = 24

null_h = 'bug resolution time is 24hr'
alt_h = 'bug resolution time is not 24hrs, may increase/ decrease'
risk = 0.05

mean_diff = sample_mean - pop_mean
sample_std_err = sample_std / sample_size ** 0.5

z_score = round(abs(mean_diff / sample_std_err),2)
print(f"\nZ SCORE {z_score}")

"""
this is a two tailed test (z_critical = stat.norm.ppf(1 - risk / 2))
"""
critical_z = 1.96
p_value = round(2 * ( 1 - stat.norm.cdf(z_score)),2)
print(f"\nP Value : {p_value}"
      f"\nAlpha Value : {risk}")


if(z_score > critical_z ):
    print(f"\nReject the Null Hypothesis, {alt_h}")
else:
    print(f"\nWe fail to reject Null Hypothesis, that is {null_h}"
          f"\nWe accept Alt Hypothesis, {alt_h}")



