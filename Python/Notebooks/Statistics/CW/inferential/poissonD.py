"""
used to model the probability of a certain number of events, occuring within a
a fixed interval of time or space, given that these events, happen within a known
constant average rate, Independently of each other.

Characteristics :
    > Discrete distribution :
        Describes rare events
        each occurences is independent of occurence of others.
        It Describes descret occurences over an interval.
        The occurence at each interval can range from 0 to infinity. [ ∞ ]
        expected number occurences must hold constant through out the experiment.

Calculate the probability of getting exactly 7 customers in one hour
when the average arrival rate is 10 customers per hour.
"""
from scipy.stats import poisson
lambda_avg = 10
k = 7

probability = round(poisson.pmf(k, lambda_avg),2) * 100
print(f"Probability : {probability} %")

