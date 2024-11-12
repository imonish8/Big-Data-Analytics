lambda_avg = 5
k = 3

from scipy.stats import poisson

probability = round(poisson.pmf(k, lambda_avg),2) * 100
print(f"Probability : {probability} %")