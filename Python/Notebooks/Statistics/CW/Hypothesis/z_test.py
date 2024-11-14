from scipy.stats import norm
import numpy as np

def single_sample_z_test_mean(sample, pop_mean, pop_std, alpha = 0.05):
    sample_mean = np.mean(sample)
    sample_size = len(sample)
    std_err = pop_std / sample_size ** 0.5
    z_score = (sample_mean - pop_mean) /  std_err

    critical_z = norm.pdf((1 - alpha)/2)
    p_value = 2 * (1 - norm.cdf(abs(z_score)))

    if(z_score > critical_z):
        print(f"reject null hypothesis")
    else:
        print(f"Fail to reject Null hypothesis")


sample_data = [50, 52, 53, 48, 47, 50, 52, 49]
pop_mean_ = 50
pop_std_ = 5

single_sample_z_test_mean(sample_data, pop_mean_, pop_std_)

"""
critical z-value is calculated to define the cut off points, for a statistical test, 
determining the critical region, beyond which we would reject the null hypothesis, 
steps to determine critical z value

> the significance level alpha represents the probability of rejecting the null hypothesis
    when it is actually true. TYPE I

> Common choices of alpha are 0.05 or 

> step 2 for a two tailed test :
in many cases, we perdorm a two tailed test, which tests, if the sample mean is,
sifnificantly different from the population mean.
in either direction, for a two test, we split alpha in half, allocating half od the signifcancel level to each tail.

> step 1 :
    using standard normal distribution
    the cirtical z value is the point on the standard normal distribution that corresponds to cumaltive of 1 - alpha/2
    this givrs a cut off 
    beyond which the test fall into rejection region.
    

P VALUE ;
    - The proabability of obtaining, a test statistics atleast as extreme as the one observed
    assuming null hypothesis is true.
    - It provides a measure of the strength of evidence against the null hypothesis.
    - A Smaller p value indicates, stronger evidence.
    - in a z test, the p value corresponds to the probability of oberving, a z-score as extreme as,
    the one computed from, sample data.
    - Formayla 
        p = 2 * (1 - cdf(abs(z_score)))
        cdf -> cumalative distribution function.
        
        for ome tailed test
        p = 1 - cdf(abs(z_score))

t - test of mean is statistical test, used to determine, if there is significant difference between the sample mean
and a known or hypothesis pop_mean, especially when the pop_std_dev is unknown.

use case : when working with samll sample sizes usally n < 30. or pop_std_dev is unkown.


types t-test 
    1. ttest_1samp :
        it tests if the mean of a single sample, is significantly different from a known or 
        hypothesised pop_mean
        
        std_err_sample = sample_std_dev / n ** 0.5
        t = mean_sample - pop_mean / std_err
    
    assumptions of one sample t-test
        - data is normally disyributed, this test assusmes that, data follows a normal distribution,
        - for a larger samples, the central limit theorem, implies that, the sample mean will be
            approx normal, even if the population isn't.
        - Independence : observations should be independent od each other,  

        

"""



