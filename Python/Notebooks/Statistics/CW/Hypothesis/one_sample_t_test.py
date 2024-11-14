import numpy as np
import scipy.stats as stats

def one_sample_t_test(sample, pop_mean, alpha=0.05):
    sample_mean = np.mean(sample)
    n = len(sample)
    sample_std = np.std(sample, ddof=1)
    mean_diff = sample_mean - pop_mean
    std_sample_error = sample_std / np.sqrt(n)
    t_test = mean_diff / std_sample_error
    df = n - 1


    critical_t = stats.t.ppf(1 - alpha/2, df)
    p_value = 2 * (1 - stats.t.cdf(abs(t_test), df))


    if p_value < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")


    print(f"t-statistic: {t_test}, critical t: {critical_t}, p-value: {p_value}")

# Example usage
sample = [12, 15, 14, 10, 13, 12, 15, 16]
pop_mean = 13
one_sample_t_test(sample, pop_mean)
