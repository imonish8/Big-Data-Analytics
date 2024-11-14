"""
This test compares the mean of two independent groups.
to see if there is, a significant

    - INdependent two sample t-test compares the means of  two independent groups,
    - To determine if there is a statistically significant differences between them
    - the two sample t-test is commanly used, when you have two seperate groups,
        and want to test, if there means differ.
    - eg., comparing avg test scores of two different classes,
    eg., testing a effectivness of new drug, by comparing the treamtent group and controlled group.

Assumptions :

    1. observations in each group, must be independent of each other,normality,
    the data in each group, should follow a normal distribution. especially for small samples

    2. Equal variances :
        the variances of two groups, are assumed to be equal, this is called, pooled
        t-test.


"""

from scipy.stats import ttest_ind

groupA = [ 12, 15, 14, 10, 13, 15, 16]
groupB = [14,16, 13, 18, 19, 17, 16, 18]

test, p = ttest_ind(groupA, groupB)

alpha = 0.05

if(p >= alpha):
    print('Accepting H0')
else:
    print("Reject H0")



