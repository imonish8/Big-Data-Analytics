"""
Bell shaped curve
common prabability distrubution a central average or mean its often called a bail curve
because its shape which is symmetric



Suppose the average commute time to work is 30 min, with a std
deviation of 5 min.
1.Generate a distribution of commuting times
2.Calculate the probability of commuting times falling
within certain ranges.'''
"""
from tkinter.ttk import Label

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean_avg = 30
std = 5

comm_time = np.linspace(10,50, 1000)

PDF = norm.pdf(comm_time, mean_avg, std)

plt.plot(comm_time,PDF, color='blue')
plt.title("Normal Distribution of Commute Time")
plt.xlabel("Commute Time (minutes)")
plt.ylabel("Probability Density")
plt.axvline(mean_avg, color='red', linestyle='--', label='Mean Commute Time')
plt.axvline(mean_avg+std, color='yellow', linestyle='--', label='Standard Deviation + Mean')
plt.axvline(mean_avg-std, color='yellow', linestyle='--', label='Standard Deviation - Mean')

plt.legend()fw
plt.show()

print(PDF)

