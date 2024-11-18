"""
 Applying Bayes' Theorem to Weather Forecasting

   **Question**: A weather forecasting model predicts
   that there’s an 80% chance of rain on days when it’s cloudy.
   However, it’s cloudy only 30% of the time, and
   overall it rains 20% of the time.

   Using Bayes' Theorem, calculate:
   - The probability that it’s cloudy given that it’s raining.
   - Interpret what this probability means in the context of forecasting and cloud cover.



"""

P_rain_cloudy = 0.8
P_cloud = 0.3
P_rain = 0.2

P_Cloud_Raining = P_rain_cloudy * P_cloud / P_rain

print(f"Probability of it is cloudy when given that raining : {P_Cloud_Raining}")
