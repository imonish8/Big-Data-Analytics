"""
A retail company wants to understand customer spending paterns
to improve its marketing strategies.They collect data on the daily
spending of customers over a year.However,they notice that some days have
significantly higher spending due to sales events or holidays, while
regular days show moderate to low spending.
The comapny wants to anlyze whether the spending distribution is symmetrical
or skewed to make targeted marketing decisions.If spending is heavily
skewed the comapny will conside
tailoring promotions to specific
customer segments or revising timing of their sales campaign.
Tasks:
1.Calculate the Skewness
2.Interpret skewness value
3.Business Strategy recommendations:Based on skewness results,propose
changes in marketing strategies such as adjusting discounts,optimizing
 ad budgets,or setting special dates.
 Dataset:
 generate sample data

 box plots tell q1 q2 q3 and outlies whioch lies on the extremes of the box plot upper and lower as well.

"""
import pandas as pd
import numpy as np
from scipy.stats import skew



daily_spend  = np.random.normal(loc=100, scale=30, size=365)

sales  = np.random.normal(loc=100, scale=30, size=365)

yearly_spends = np.concatenate((daily_spend, sales))
#print(np.count_nonzero(yearly_spends))
framed = pd.DataFrame(yearly_spends, columns=['Spending'])
spending_skewness = round(skew(framed['Spending']))
#print(framed)
print(spending_skewness)

if( spending_skewness > 0):
    print("Positice Skewness \nCustomer Spending High \nTailor the Promotion on specific days")
elif( spending_skewness < 0):
    print("Negatice Skewness \nCustomers spending low \nPromotion needed")
else:
    print("Skewness is Zero \nSpending distribution is Symmetrical \nmaintain consistency.")





