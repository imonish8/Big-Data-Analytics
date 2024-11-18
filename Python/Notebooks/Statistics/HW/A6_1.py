"""

1. Conditional Probability in Real-World Scenarios

   **Question**: A medical test has a 98% probability of detecting a disease
    if a person has it (true positive rate) and a 2% chance of a false positive
    (detecting the disease when it's not there). In a certain population,
    1% of people have the disease.

   Using Bayes' Theorem:
   - Calculate the probability that a person has the disease given that they tested positive.
   - Explain how the prevalence of the disease affects the result and interpret the findings.


"""

P_true_positive = 0.98
P_false_positive = 0.02
prevelence = 0.01
P_no_disease = 1 - prevelence

# tested positive
P_test_positive = (prevelence * P_true_positive) + (P_no_disease * P_false_positive)


#according to bays need to relate 2 totally different events,
# P(DIESASE | TRUE_POSITIVE)


disease_positive_tested = round((P_true_positive * prevelence ) / P_test_positive,2) * 100
print(disease_positive_tested, "%")

