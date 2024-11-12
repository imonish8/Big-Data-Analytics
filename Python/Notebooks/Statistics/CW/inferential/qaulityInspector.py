"""
A quality control inspector at a factory finds that, on average
5% of the manufactured items are defective.The inspector randomly selcts
20 items from the production line.What is the probaility that exactly 2
of the selected items are defective?

"""
from scipy.stats import binom

n = 10
k = 7
p = 0.05


prob = binom.pmf(k, n, p)
print(f"Probability of exactly 2 defective items: {prob:.4f}")