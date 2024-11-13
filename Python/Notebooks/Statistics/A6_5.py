"""
5. Comparing Marginal and Conditional Probabilities in Health Screening

   **Question**: In a study, 5% of individuals have a certain condition.
   A test for the condition has a true positive rate of 90% and
   a false positive rate of 8%.

   Calculate:
   - The marginal probability that an individual will test positive (regardless of whether they have the condition).
   - The conditional probability that an individual has the condition given a positive test result.
   - Compare the marginal and conditional probabilities and explain the impact of the base rate on your findings.

"""
P_Condition = 0.05
P_noCondition = 1 - 0.05
P_positive = 0.9
P_Negative = 0.08

P_Indivisual_positive = round((P_positive * P_Condition) + (P_Negative * P_noCondition),2) * 100
print("Marginal Probability Indivisual ",P_Indivisual_positive, "%")

P_Condition_positive = round((P_positive * P_Condition / P_Indivisual_positive),6) * 100
print(f"Conditional Probability Indiviual has condition considering he/she is positive : {P_Condition_positive} %")


"""
Interpretation : Still the 5% indivisual having chances of getting false positive after result
because likelihood of getting the condition in the first place is 37% which is below the 
50% chance of getting the disease even after tested positive.
So many 5% tested positive might have false positive.
"""





