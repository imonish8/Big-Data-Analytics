"""
A soft drink seller selling bottle with 600ml volume

alternate hypothses : H is not equal to 600 or less than 600.
null : H is greater than 600.

In statistics type 1 and type II Error are two types
of mistakes we can make when testing hypothesis

    > False Positive -- type I
        1. This happens when we reject a true null
        hypothesis, means you think there effect and difference when there isnt
        one actually.

    > Type II false negative:
        1. This occurs when we fail to reject a false null hypothesis,
        2. here you think there is effect or difference  when there actually is one.
        you are missing something thats really there.
        h0 = volume
        eg., volume is greater than 600, customer saying it is lower.

    steps to formulate hypothesis:
        1. Developing clear research problem
        2. calculate hu and h0
        2. determine approx statistics test.
        4. Gatjering data
        5. state secision
        6. choose type 1 error. (alpha = 0.05)
        7. calculate stat
        8. Conclusion

    p-value is measure to determine null hypothesis
    alpha < p-value ?? reject null hypo
    alpha > p-value ?? accept the null hypothesis


    > P-value is a number in statistics that helps you decide, waether your results are
        meaningful or happend by chance
        tells how likely it is to get obsered results if null hypothesis were actually
        true.
        A Low p-value [typically less than alpha] strong evidence against null hypo.
            implies you should reject null hypothesis.
            Results are are unlikely to have happened by random chance alone.
            this means, you might found something significant, may consider rejecting
            null hypothesis.

        A High p-value [greater than alpha] suggests that results could easily have happend by chance.
            so no strong eveidence against null hypothesis,



    > Confidence interval :
        range of values that is likely to contain, true value of population parameter.
         with a certain level of confidence

       > Steps to cal:
            1. for a 95% CI Mean : (zsxore - 1.96)
                collect sample data, gather a random sample data from the population

            2. Calculate the sample mean x avg of sample data.
                pop mean (mu)

            3. calculate sample std dev. (s)
                pop std dev is sigma
                tells how spread out the values in sample are.

            4. calculate sample std error :
                SE = S / n ** 0.5
                this measures the precision of sample mean, as an estimate of
                the population mean

            5. find z-score
                the score you use depends on the sample size, for large
                samples, n > 30 you can use the z-score. 1.96 with CI 95%

                when n < 30 or either WHEN pop std dev is unknown you use the t-score.
                t = x - mu / std err

            6. calculate margin error
               ME  = Z * SE
               or T * SE.

            7. Calculate the lower bound : x` - ME
            8. uPPER Bound = x` + ME

               CI : [Lower_bound, upper_bound]









"""
from plotnine import geom_map
from streamlit.runtime.runtime_util import get_max_message_size_bytes

sample_size =  50
avg_wt = 150
s = 10

z_score = 1.96
se = s / sample_size ** 0.5
mar_err = se * z_score
lower_ = avg_wt - mar_err
upper_ = avg_wt + mar_err

print(f"CI between [{lower_}, {upper_}]")


