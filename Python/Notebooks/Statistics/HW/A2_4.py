import numpy as np
from scipy.stats import mode


def salary_analysis(salaries):
    mean_salary = np.mean(salaries)
    median_salary = np.median(salaries)

    mode_result = mode(salaries, keepdims=True)  
    mode_salary = mode_result.mode[0] if mode_result.count[0] > 0 else "No mode"

    print(f"Average Salary (Mean): ${mean_salary:.2f}")
    print(f"Typical Salary (Median): ${median_salary:.2f}")
    print(f"Most Common Salary (Mode): ${mode_salary}")

salaries = [45000, 52000, 60000, 45000, 72000, 52000, 68000, 52000, 80000, 45000]
salary_analysis(salaries)