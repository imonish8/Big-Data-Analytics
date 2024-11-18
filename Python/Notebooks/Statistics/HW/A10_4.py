import scipy.stats as stats

strategy_a = [100, 120, 130, 125, 140, 150, 145, 135, 110, 115]
strategy_b = [90, 95, 100, 105, 115, 120, 110, 95, 100, 105]


u_statistic, p_value = stats.mannwhitneyu(strategy_a, strategy_b, alternative='two-sided')

print(f"U-Statistic: {u_statistic}")
print(f"P-Value: {p_value}")


alpha = 0.05
if p_value < alpha:
    print("We reject the null hypothesis: Significant "
          "difference between the strategies.")
else:
    print("We fail to reject the null hypothesis: No significant difference "
          "between the strategies.")

