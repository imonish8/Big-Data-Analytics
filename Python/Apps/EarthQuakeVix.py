import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/imonish8/Desktop/Big-Data-Analytics/Python/PycharmProjects/earthquakes_2023_global.csv")
# Assuming 'time' column exists and is in datetime format
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df['Year'] = df['time'].dt.year
df['Month'] = df['time'].dt.month
df['Day'] = df['time'].dt.day

def plot_magnitude_distributition():
    fig.clear()
    sns.histplot(df['mag'], bins=50, kde=True, ax = fig.add_subplot(111))
    canvas.draw()

def plot_earthquakes_per_year():
    fig.clear()
    eq_per_year_plot = eq_per_year = df['Year'].value_counts().sort_index()
    ax = fig.add_subplot(111)
    ax.plot(eq_per_year_plot.index, eq_per_year_plot.values, marker = 'o')

root = tk.Tk()
root.title("Earthquake Data Visualisation")

mainframe = ttk.Frame(root, padding = '10')
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

plot_button1 = ttk.Button(mainframe, text="Magnitude Distribution", command=plot_magnitude_distributition)
plot_button1.grid(column=0, row=0, padx=5, pady=5)


#plot_button2 = ttk.Button(mainframe, text="Earthquakes Per Year", command=plot_earthquakes_per_year)
#plot_button2.grid(column=1, row=0, padx=5, pady=5)

fig = plt.Figure(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=mainframe)
canvas.get_tk_widget().grid(column=0, row=1, columnspan=2)

root.mainloop()