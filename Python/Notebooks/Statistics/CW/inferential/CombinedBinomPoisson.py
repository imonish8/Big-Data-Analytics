"""
A bookstore has, on average, 3 customers entering every 15 minutes.
However,only 20% of customers make a purchase.If 4 customers enter in a
given 15-minute period,what is the probability that exactly 1 of
them will make a purchase?
"""
from scipy.stats import poisson, binom

lambda_avg=3
customers_entered=4
prob_4_customers=poisson.pmf(customers_entered,lambda_avg)
pro_prchase=0.2
no_purchase=1
pro_1_purchase_given_4=binom.pmf(no_purchase,customers_entered,pro_prchase)
combined_probability=round(prob_4_customers+pro_1_purchase_given_4,1) * 100
print(combined_probability, " %")