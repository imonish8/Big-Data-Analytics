"""
A customer service center receives, on average, 10 calls per hour.
   - a) What is the probability that exactly 8 calls will be received in a given hour?
   - b) What is the probability that at least 12 calls will be received in an hour?

"""

from scipy.stats import poisson

lambda_rate = 10
k_exact = 8
k_atleast = 11

probability = round(poisson.pmf(k_exact, lambda_rate),2) * 100
probability_12 = round((1 - poisson.cdf(k_atleast, lambda_rate)),2) * 100


print(f"Probability of recieving *EXACTLY* 8 calls in given hour is : {probability} % ")
print(f"Probability of recieving *ATLEAST* 12 calls in given hour is : {probability_12} % ")