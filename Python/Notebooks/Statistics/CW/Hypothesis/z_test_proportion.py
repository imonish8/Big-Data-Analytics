"""
proportional test used to determine, weather the proportion of sample differes sign
nificantly from a hypothesised population proportion, this test is commonly used,
when dealing with categorical data, such as yes or no answers, to assess weather the observed proportion
 matched an expected on

 a z test proportional is typically used when data have categories, the two possible
 outcomes, also when you want to test, if a sample proportional `p` is significantly different from
 a population proportion,
p -> sample prop
p` -> pop prop
 z = p - p` / p (1- p`) / n ** 0.5

Assumptions :
    1. Sample size : The sample size should be large enough,
        so that, both the n * p is zero and n * 1 - p` are atleast 5
        - This ensures, the sampling distribution of the proportion `s`
        - approx normal,
    2. Random sampling :
        - The sample should be randomly selected from population,



"""

from statsmodels.stats.proportion import proportions_ztest
p = 0.60
num = 70
n = 100
test, p = proportions_ztest(num, n, value=p)
alpha = 0.05
if p > alpha:
    print('accept null h')
else:
    print('reject')



p1 = 40 / 100
p_pop = 0.50
n = 100
a = 0.05


