"""
FOR A ONE TAIL TEST
"""

alpha = 0.01
z_value_critical_onetail = 2.33

statement = "company sells drug2 claims 30% better compare to previous drug0"
null_h = "drug2 is not changed"
alt_h = ("drug2 is better more than 30%")


"""assume z_score_calculated = 3.33"""
z_score_calculated = 3.33
print("\nOne TAILED EXAMPLE WHEN ALPHA IS 0.01")
if(abs(z_score_calculated) > z_value_critical_onetail):
    print(f"Reject Hypothesis which states that, {null_h}")
else:
    print(f"Fails to reject Hypothesis which states that, {null_h}")


""" FOR TWO TAIL TEST """

print("\nTWO TAILED TEST")
z_value_critical_twotail = 2.58

print("\nNONE TAILED EXAMPLE WHEN ALPHA IS 0.01")
if(abs(z_score_calculated) > z_value_critical_twotail):
    print(f"Reject Hypothesis which states that, {null_h}")
else:
    print(f"Fails to reject Hypothesis which states that, {null_h}")

# null mu = 0
# alt mu >=30
# Conlusion is this that both the z_critical values in two and one tail test is more
#which means both test are not enough against Null Hypothesis. need more advance test
# to reject Null hypotheis.



