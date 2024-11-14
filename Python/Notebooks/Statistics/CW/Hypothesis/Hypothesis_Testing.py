"""

Sampling is a way of taking sample to make observations and draw conclusions
about the whole poplulation, without needing to look at every single member.


Adv :
    > Reduce cost
    > saves time.
    > make predictions about whole poppulation.

:type
    > random sampling :
        every indivisual has an equal chanc eof  being selected.
    > Stratify Sampling:
        population is divided into subgroups.
        samples are taken from, each subgroup
    > Systematic :
        select all person in list.
    > Cluster sampling :
        poplulation is divided into clusters.
        when some clusters are randomly selected.
    > central Limit Theorom, is fundamental concept in statistics,
        that explains, why averages from different samples, tend to follow,
        a predicitable pattern. It says that, if you take enough random samples,
        from any population no matter the population looks ilike the average of
        those samples, will follow, normal bell shaped distribution. if the sample size is
        large enough.

    > Single Sample z-test  of mean:
        z = x` - mu / sigma * (n ** 0.5)
        x` -> sample mean
        mu -> pop mean
        sigma => pop std dev
        n -> size

        a single sample z test of mean is a statistical test, that is
        used to determine, if the mean of the sample, is significantly different, from a known pop
        mean, this test is commonly used, when we have a large sample size\

        - TEST Checks if our sample mean is a just a result of random chance or if it is,
          significantly different, from the pop mean, we are comparing it to.

    > steps to compute z test.

        1.calculate sample mean
        2. meaasure mean of sample
        3. calculate the z score.. this score tells us how far the sample mean isfrom the pop mean, in terms of
            standard errors
        4. compare the z score to a critical value,
        5. for a one tailed test at 95 CI, the critical z value is -1.645
            if the calculated z score is less than, -1.645

        In hypothesis testing one tailed or two tailed test
            refers to the direction of the test, how we assess the
            significance of the results based on our hypothesis.
        One tailed test assess ;
            wheather the sample mean is significantly higher or lower than the hypothesised pop mean,
            in one specific direction,

        A Two tailed test assess weather the sample mean is significantly different
        from the hypothesized pop mean, in either direction.
        Use a two tailed test, whean you want to check for, any significant difference.
        without specifying a direction.

        The effect could be either direction. i.e. The test could reveal,
        if the value is significantly higher or lower. than the hypothesised mean

        1. suppose a pharmaseutical company claims that, its drug has average effect
        strength of 50units, you want to see if a new batch of drugs has different effect strength.
        formulate null and alternate hypothesis
         mu = 50
         mu =! 50
         two tailed hypothesis.



"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import mean, std
from numpy.ma.extras import average

population = np.random.normal(50000, 10000, 100000)
sample_size =500
sample = np.random.choice(population, sample_size, replace=False)
#print(sample)

mean_p = mean(population)
mean_s = mean(sample)
std_p = std(population)
std_s = std(sample)

print("Mean Comparison ",mean_p, mean_s)
print(f"\n STD : {std_p} {std_s}")

sample_size1 = 100
num_samples = 100
sample_mean = []
for i in range(num_samples):
    sample = np.random.choice(population, sample_size1, replace=False)
    sample_mean.append(sample.mean())

mean_sample = average(sample_mean)
std_sample = std(sample_mean)
print(mean_sample)
print(std_sample)

plt.hist(sample_mean, bins= 30)
plt.title("Sampling mean")
plt.xlabel(" mean sample")
plt.ylabel('frequency')
plt.axvline(mean_sample, color='red', linestyle='--', label='Mean Commute Time')
plt.show()






