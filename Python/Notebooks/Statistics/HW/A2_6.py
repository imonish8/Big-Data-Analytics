import numpy as np

def salary_quartile_analysis(salaries):
    # Quartiles
    q1 = np.percentile(salaries, 25)
    q2 = np.percentile(salaries, 50)
    q3 = np.percentile(salaries, 75)

    below_q1 = [s for s in salaries if s < q1]
    between_q1_q2 = [s for s in salaries if q1 <= s < q2]
    between_q2_q3 = [s for s in salaries if q2 <= s < q3]
    above_q3 = [s for s in salaries if s >= q3]

    print(f"Q1: ${q1:.2f}, Q2 (Median): ${q2:.2f}, Q3: ${q3:.2f}")
    print(f"Number of employees below Q1: {len(below_q1)}")
    print(f"Number of employees between Q1 and Q2: {len(between_q1_q2)}")
    print(f"Number of employees between Q2 and Q3: {len(between_q2_q3)}")
    print(f"Number of employees above Q3: {len(above_q3)}")

    ranges = [
        ("Below Q1", below_q1),
        ("Between Q1 and Q2", between_q1_q2),
        ("Between Q2 and Q3", between_q2_q3),
        ("Above Q3", above_q3)
    ]
    print("\nSalary Summary:")
    for label, group in ranges:
        avg = np.mean(group) if group else 0
        print(f"{label}: Average Salary = ${avg:.2f}")

salaries = [
    60, 70, 75, 85, 95, 100, 110, 120, 150, 160,
    180, 200, 250, 300, 350, 400, 450, 500, 550, 600,
    650, 700, 750, 800, 850, 900, 950
]
salary_quartile_analysis(salaries)