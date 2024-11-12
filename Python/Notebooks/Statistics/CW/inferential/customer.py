"""

''suppose a customer service representative tries to reach
out to 10 clients daily, and each call has 30% chance of the client pickinng
up.Calculate the probability of exactly 3 clients answering.
"""

from scipy.stats import binom



n = 10
k = 3
p = 0.3


probability = round(binom.pmf(k, n, p),2) * 100
print(f"Probability : {probability} %")

"""
mean computation :
    > ų = np
    > б = sqrt(nqp)
"""
