"""
 Spam Classification with Multiple Words

   **Question**: Extend the email spam example where now
   we’re looking at the presence of two words: "Offer" and "Free".

   Suppose:
   - 40% of emails are spam.
   - 65% of spam emails contain "Offer" and 80% contain "Free".
   - 20% of non-spam emails contain "Offer" and 5% contain "Free".
   - 45% of spam emails contain both "Offer" and "Free".
   - 3% of non-spam emails contain both "Offer" and "Free".

   Calculate:
   - The probability that an email is spam given it contains "Offer".
   - The probability that an email is spam given it contains "Free".
   - The probability that an email is spam given it contains both "Offer" and "Free".

"""
P_Spam = 0.40
P_NotSpam = 1 - P_Spam
P_Offer_given_Spam = 0.65
P_Free_given_Spam = 0.80
P_Offer_and_Free_given_Spam = 0.45
P_Offer_given_NotSpam = 0.20
P_Free_given_NotSpam = 0.05
P_Offer_and_Free_given_NotSpam = 0.03

P_Offer = (P_Offer_given_Spam * P_Spam) + (P_Offer_given_NotSpam * P_NotSpam)

P_Spam_given_Offer = (P_Offer_given_Spam * P_Spam) / P_Offer
print(f"P(Spam | Offer) = {P_Spam_given_Offer:.4f}")

P_Free = (P_Free_given_Spam * P_Spam) + (P_Free_given_NotSpam * P_NotSpam)

P_Spam_given_Free = (P_Free_given_Spam * P_Spam) / P_Free
print(f"P(Spam | Free) = {P_Spam_given_Free:.4f}")

P_Offer_and_Free = (P_Offer_and_Free_given_Spam * P_Spam) + (P_Offer_and_Free_given_NotSpam * P_NotSpam)

P_Spam_given_Offer_and_Free = (P_Offer_and_Free_given_Spam * P_Spam) / P_Offer_and_Free
print(f"P(Spam | Offer and Free) = {P_Spam_given_Offer_and_Free:.4f}")