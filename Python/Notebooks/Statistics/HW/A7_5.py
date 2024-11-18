"""
Suppose the daily water consumption in a city is skewed to the right with a mean of 150 liters and a standard deviation of 30 liters.
   - a) Take 1,000 random samples of size 50 each and calculate the mean of each sample.
   - b) Plot the histogram of the sample means.
   - c) Based on the plot, describe how the shape of the sampling distribution of the sample mean compares to the shape of the original population.

"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
mean_ = 150
to_make_std = mean_ - 20
std_ = 30
pop_size = 10000
pops_ = np.random.exponential(scale=30, size=pop_size) + to_make_std

samples_ = 1000
size_ = 50

sample_ = np.random.choice(pops_, size_, replace=False)
mean_consumption = round(np.mean(sample_),2)
print(f"sample mean : {mean_consumption} ")
arrays_1000_samples = []
for i in range(samples_):
    each_sample = np.random.choice(pops_, size_, replace=False)
    mean_each_sample = np.mean(each_sample)
    arrays_1000_samples.append(mean_each_sample)

mean_sample_means = np.mean(arrays_1000_samples)
std_error = 30 / np.sqrt(size_)

plt.figure(figsize=(10, 6))
sns.histplot(arrays_1000_samples, bins=30, kde=True, color="skyblue", edgecolor="black")
plt.axvline(mean_sample_means, color="red", linestyle="--", label="Mean")
plt.axvline(mean_sample_means + std_error, color="orange", linestyle="--", label="+1 SD")
plt.axvline(mean_sample_means - std_error, color="orange", linestyle="--", label="-1 SD")
plt.axvline(mean_sample_means + 2 * std_error, color="green", linestyle="--", label="+2 SD")
plt.axvline(mean_sample_means - 2 * std_error, color="green", linestyle="--", label="-2 SD")

plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.title("Sampling Distribution of the Sample Mean with Standard Deviations")
plt.legend()
plt.show()

"""
"The Graph Plot woth seaborn shows mean skewed slightly to right with 163.11 and"
 2 std deviation with orange and green.


"""


