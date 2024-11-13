"""

You are working on a simple spam classification model for emails.
Given ceratin words in an email,you want to determine the probability that
the email is spam.
Data:
Based on historical data:
40% of emails are spam
60% of emails are not spam
For the word "Offer"
70% of spam emails contain the word offer
10% of non-spam emails contain the word offer
Task:
Using Bayes theorem calculate the probability that emails
is spam,given that it contains the word offer.

"""


P_spam = 0.40
P_not_spam = 0.60
P_offer_given_spam = 0.70
P_offer_given_not_spam = 0.10


P_offer = (P_offer_given_spam * P_spam) + (P_offer_given_not_spam * P_not_spam)

P_spam_given_offer = round((P_offer_given_spam * P_spam) / P_offer,2) * 100


print(f"The probability that the email is spam( word 'Offer') is: {P_spam_given_offer:} %")