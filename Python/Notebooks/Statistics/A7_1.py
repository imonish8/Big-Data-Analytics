"""
A factory produces bulbs, and each bulb has a 5% chance of being defective. Out of a batch of 50 bulbs:
   - a) What is the probability of finding exactly 3 defective bulbs?
   - b) What is the probability of finding at most 2 defective bulbs?


"""

p = 0.05
n = 50
k = 3

from scipy.stats import binom

probability = round(binom.pmf(k,n,p),2) * 100
print(f"Probability for finding Exactly 3 Bulbs defective is : {probability} %")
