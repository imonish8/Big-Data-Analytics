from scipy.stats import binom
"""
''Imagine you flip a coin 10 times, and you want to know the
probability of getting heads exactly 6 times.'''
"""

n = 10
x = 6
p = 0.5

probability = round(binom.pmf(x,n,p),1)
print(f"Probability is : {probability}")

"""
assumptions :
    > Experiment Involves, n identitical trials
    > Each trial has, only two possible outcomes denoted as success or fail.
    > each trial is independent of previous trials
    > terms P & Q, remains constant, through out the experiment.
    > 
"""



