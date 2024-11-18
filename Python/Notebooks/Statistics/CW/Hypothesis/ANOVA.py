"""
STAatistical technique used to determine,
if there are, signidicant differences between the means of three or more groups

anova tests wather the means of different groups, are equal by examningin the variances
within each group

and variance between the group

it is used to determine if atleast one group mean as different from the others

one way ANOVA
    - This tests the impact of a single factor, of multiple grpips
    Two annova
        test the impact of two factors simultaneously, i can determine,

        Assumptions of annova : indepec
        - samples are indepennt of each other,
        - Normality, the data in each grpup are normally distributed,

        Each group has similar variance

        Steps in performing one way anova.

        Define the Null Hypothesis and null hypothesis

        Note this, Null and
        Calculate between group variance. measure how much variance exists between group means,

        step 3 :
            measures the variablity within each group.

        formula :

        step 4 :
        compute the f statistics

        formula :

        MSB ->

        step 5
        compare the f stat to a critical value from the f distribution,
        to determine significance, if the f stat is latger than the critical values,
        reject the null hypothesis.

        most powerfull mac i can get now at rate :
            > $7,548.98
            > name : 14‑inch MacBook Apple M4 Max chip
            with 16‑core CPU, 40‑core GPU, 16‑core Neural Engine,
            Nano texture display,
            128GB unified memory
            8TB SSD storage








"""
import numpy as np

from CW.Hypothesis.independent_test import alpha

"""
import numpy as np
import  scipy.stats as stat
import  pandas as pd
from pygments.lexers.robotframework import IMPORT

A = [52,55,34,55,64,65,34,23,44]
B = [34,65,34,23,78,89,64,22,78]
C = [23,53,67,23,86,23,89,45,87]

DATA = [A,B,C]

f_stat, p_val = stat.f_oneway(A,B,C)

alpha = 0.05
if p_val > alpha:
    print(f"\nf stat is {f_stat} , pval : {p_val}"
          f"\nfail to reject nULL HYPOTHESIS")

else:
    print(f"\nf stat is {f_stat} , pval : {p_val}"
          f"\nreject nULL HYPOTHESIS")

"""
"""
Steps for Two Way ANNOVA :
    1. Gather data and formulate hypotheis.
    2. compute means, calculate, grand mean, 
    3. Patition the variance, tot
    
    total variability = sst 
    ssb between group variablity, 
    5 . Mean square.
    
"""

"""
print("\n TWO WAY ANOVA")

import  statsmodels.api as sm
from statsmodels.formula.api import ols

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stat


data = {
    "Method": ["A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B"],
    "Time": ["1 Hour", "1 Hour", "1 Hour", "2 Hours", "2 Hours", "2 Hours",
             "1 Hour", "1 Hour", "1 Hour", "2 Hours", "2 Hours", "2 Hours"],
    "Score": [50, 55, 53, 70, 73, 72, 52, 54, 51, 68, 67, 69]
}


df = pd.DataFrame(data)


model = ols('Score ~ C(Method) + C(Time) + C(Method):C(Time)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

"""
"""
chisquare test is non parametics test.

used to determine,
"""
"""

MALE_CAR = 20
MALE_BIKE = 40
MALE_PT = 40
MALE_TOTAL = 100

F_CAR = 30
F_BIKE = 10
F_PT = 60
F_TOTAL = 00

CAR = 0
PT = 0
BIKE = 0
TOTAL = 0

#
# 1 FORMULATE HYPOTHESIS NULL : GENDER AND TRANSPOT DEPENDENT,GENDER AND TRANSPORT MODE ARE INDEPENDENT.
# 2 CALCULATE EXPECTED FREQUENCIES.
# 3 CALCULATE TRI CHI STATISTICS.
# 4
"""



"""
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stat
OBS = np.array([[20,30], [40, 10],[30,40]])
test1, p_val, expect = stat.chi2_contingency(OBS)

alpha = 0.05
if p_val < alpha:
    print("Reject")
else:
    print("Fail to reject")






> A U-test 
    mann whitney u test non parametric u test. statistical test, used to determine, 
    where there is significant difference.
    it is commonly used, 
    when the data is ordinal, the data is ordinal, interval or ratio, the distribution may not be normally distributed
    
    steps to compute u-test, 
    1 > combine and rank them in ascending order,
    2 > compute the rank sums for each group. R1 R2.. SO ON...
    3 > compute the u-statistics, for each group.
    4 > Rank sum of two groups.
    5 > formula 
    6 > 
    
"""

groupA = [30, 29, 39,43, 23]
groupB = [30, 22, 34,21,11]

from scipy.stats import  mannwhitneyu
TEST, P_VAL = mannwhitneyu(groupA, groupB)

alpha = 0.05
if(P_VAL > alpha):
    print("fail to reject")
else:
    print("reject")




