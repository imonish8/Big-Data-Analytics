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




