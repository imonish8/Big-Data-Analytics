"""You have a population of 10,000 values representing product weights with an unknown mean and standard deviation. Draw a random sample of 100 values and calculate:
   - a) The sample mean and sample standard deviation.
   - b) If you take multiple samples of 100, plot the sampling distribution of the sample mean. Does it resemble a normal distribution?
   - c) Explain how this relates to the Central Limit Theorem."""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
population_weights = np.random.normal(loc=50, scale=10, size=10000)
sample = np.random.choice(population_weights, 100, replace = True )
sampleMean = np.mean(sample)
sampleSTD = np.std(sample)
multiple_sample = []
#muliple here i took 30 of size 100
for _ in range(30):
    sample_ = np.random.choice(population_weights, 100, replace=True)
    sample_MEAN = np.mean(sample_)
    multiple_sample.append(sample_MEAN)
#multiple_sample_mean = average(multiple_sample)
#multiple_sample_mean = np.mean(multiple_sample)
#plt.hist(multiple_sample, bins=30,edgecolor='k', density=True)
sns.histplot(multiple_sample, bins=30, kde=True, color="skyblue", edgecolor="black")
plt.title('checking if Normal Distribution')
mean_multiple = np.mean(multiple_sample)
plt.xlabel("Mean of 30 multiple random Samples of size 100")
plt.axvline(mean_multiple,color='red', linestyle='--', label='Mean of Multiple samples')
plt.ylabel("Frequency")
plt.show()
"""
central limit theorem tells me about the regardless of the population or size of pop.
the distribution of mean of multiple samlples will tend to approx normal.

Here in this case the plot does not Rsemble normal distribution
    because :
    > Skewness is not zero implies Distribution is not symmetry
    > more outliers on right than left.
    > a slight bump in range of multiple sample mean implies this is not a normal Distribution.
"""


