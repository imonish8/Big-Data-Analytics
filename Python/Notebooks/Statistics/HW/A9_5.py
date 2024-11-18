import numpy as np
import scipy.stats as stat


null_h = '90% of people who recieve a new vaccine are protected from a disease'
alt_h = '90% of people who recieve vaccine are not protected from disease'


x_observed = 250
x_size_observed = 300
claimed_proportion = 0.9
observed_proportion = x_observed/x_size_observed

z_score = (observed_proportion - claimed_proportion) / np.sqrt((claimed_proportion * (1 - claimed_proportion) / x_observed))
p_val = 2 * (1 - stat.norm.cdf(abs(z_score)))

alpha = 0.05
if p_val < alpha :
    decision = 'Reject Null Hypothesis, which means 90% people who had vaccinated are still not protected.'
else:
    decision = 'Accept the Null Hypothesis, which means 90% People who had vaccinated are still protected !!!'

print(decision)

