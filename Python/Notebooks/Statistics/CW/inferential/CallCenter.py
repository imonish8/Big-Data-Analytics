from scipy.stats import poisson, binom

lambda_rate = 10
k = 7



# Probability of exactly 7 calls
prob = poisson.pmf(k, lambda_rate)
print(f"Probability of exactly 7 calls: {prob:.4f}")

from scipy.stats import norm


mean = 8
std_dev = 1

lower_bound = 7
upper_bound = 9

probability = round(norm.cdf(upper_bound, mean, std_dev) - norm.cdf(lower_bound, mean, std_dev),2) * 100
print(f"Probability of working between 7 and 9 hours: {probability:.4f} %")





n = 4
p = 0.2
k = 1


probability = binom.pmf(k, n, p)


print(f"Probability that exactly one customer makes a purchase: {probability}")

from scipy.stats import poisson


lambda_ = 0.8
k = 1


probability = poisson.pmf(k, lambda_)


print(f"Probability that exactly one customer makes a purchase using Poisson approximation: {probability:.4f}")