"""
	1.	Assumptions
	•	Parametric: Assumes the data follows a normal distribution.
	•	Non-Parametric: Doesn’t need the data to follow any specific distribution.
	2.	Data Type
	•	Parametric: Works with continuous data (e.g., heights, weights).
	•	Non-Parametric: Works with both continuous and ranked (ordered) data.
	3.	Central Value
	•	Parametric: Focuses on averages (means).
	•	Non-Parametric: Focuses on the middle value (median).
	4.	Sensitivity
	•	Parametric: Gives better results if assumptions are true.
	•	Non-Parametric: Works well even if assumptions aren’t met.
	5.	Sample Size
	•	Parametric: Best for larger sample sizes.
	•	Non-Parametric: Can work with smaller datasets.
	6.	Examples
	•	Parametric: T-tests, ANOVA.
	•	Non-Parametric: Mann-Whitney U Test, Spearman correlation.

    > When to Use ?
	1.	Not Normal Data
        Use Mann-Whitney if the data isn’t normally distributed.
	2.	Ranked Data
        If the data is ranked (e.g., customer ratings), use Mann-Whitney.
	3.	Small Sample
        For small datasets, Mann-Whitney works better.
	4.	Outliers
        If there are extreme values (outliers), Mann-Whitney gives more reliable results.
	5.	Compare Medians
        Use Mann-Whitney if you care about the middle value (median) rather than the average.



"""