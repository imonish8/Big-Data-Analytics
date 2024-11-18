Before =  [220, 210, 230, 215, 225, 235, 240, 210, 200, 225]
After =  [200, 205, 215, 200, 220, 225, 230, 205, 195, 220]
alpha = 0.05

from scipy.stats import ttest_rel

test, p_val = ttest_rel(After, Before)

decision = ''
if p_val >= alpha:
    decision = 'Accept Hypothesis'
else :
    decision = 'Reject Hypothesis'

print(decision)


