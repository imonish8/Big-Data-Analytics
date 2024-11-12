"""

"""

from scipy.stats import binom

n = 15
p = 0.4
k = 6

probability = binom.pmf(k, n, p)

print(f"Probability of winning exactly 6 rounds out of 15: {probability:.4f}")


from scipy.stats import poisson

lambda_ = 5
k = 8

probability = poisson.pmf(k, lambda_)

print(f"Probability, receives exactly 8 cases in 1 hour: {probability:.4f}")



from scipy.stats import norm


mean = 70
std_dev = 10

lower_bound = 60
upper_bound = 80

probability = round(norm.cdf(upper_bound, mean, std_dev) - norm.cdf(lower_bound, mean, std_dev),2) * 100
print(f"Probability of working between 7 and 9 hours: {probability:.4f} %")
# for mean and std_dev just apply Empirical Way.



