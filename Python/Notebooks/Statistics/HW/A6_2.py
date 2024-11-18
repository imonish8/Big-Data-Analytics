"""
2. Contingency Table and Marginal Probability
   **Question**: A survey of 200 students records their preference for a programming language (Python, C++, or Java) and whether they are undergraduate or graduate students. The results are as follows:

   |               | Python | C++ | Java | Total |
   |---------------|--------|-----|------|-------|
   | Undergraduate | 50     | 30  | 20   | 100   |
   | Graduate      | 30     | 40  | 30   | 100   |
   | **Total**     | 80     | 70  | 50   | 200   |

   - Calculate the marginal probability that a student prefers Python.
   - Calculate the marginal probability that a student is an undergraduate.
   - Calculate the joint probability that a student is a graduate who prefers C++.
"""
true_python_ug = 50
true_python_g = 30
true_c_ug = 30
true_c_g = 40
true_UG = 100
total = 200

P_prefer_python = round((true_python_ug + true_python_g) / total, 2) * 100
print(f"Probability student prefer Python : {P_prefer_python} %")

P_student_is_ug = round(true_UG / total,2) * 100
print(f"Probability of Sutdent is undergad : {P_student_is_ug} %")

P_prefer_c = round(true_c_g / total,2) * 100
print(f"Probability of student prefer C++ and also graduate : {P_prefer_c} %")


