"""
A company’s employee salaries are normally distributed with a mean of $50,000 and a standard deviation of $8,000.
   - a) What percentage of employees earn more than $60,000?
   - b) If we randomly select a sample of 30 employees, what is the probability that their average salary will be between $48,000 and $52,000?

"""
import numpy as np
from scipy.stats import norm
# A
mean_ = 50000
std_ = 8000
upper_z = (60000 - mean_) / std_
n = 30
#values falling after std_dev + 2000 ie. 58000+ 2000 above 60000, right side of bell.
pro_upper = round(1 - norm.cdf(upper_z),2) * 100
print(f"Employee earning more than $60000 : {pro_upper} %")

# B
sample_mean = mean_ / (n ** 0.5 )
z_48000 = (48000 - mean_) / sample_mean
z_52000 = (52000 - mean_) / sample_mean

probability_between = round(norm.cdf(z_52000) - norm.cdf(z_48000),2) * 100

print(f"\nProbability of 30 Employees sample taken, falling between 48k and 52k : {probability_between} %")



#empirical guess is mean - 1*std = 68 so 72% approx. just a guess before calculations.
