import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("data/Iris.csv")
 
plt.plot(iris.Id, iris["SepalLengthCm"])
plt.show