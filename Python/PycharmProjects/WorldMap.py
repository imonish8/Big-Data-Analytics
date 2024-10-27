from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('earthquakes_2023_global.csv')
plt.figure(figsize=(14,8))
m = Basemap(projection = 'merc', llcrnrx= -80, urcrnrlat = 80, llcrnrlon = -180, urcrnrlon = 180, lat_ts = 20, resolution='c')
m.drawcoastlines()
m.drawcounties()
m.fillcontinents(color='orange', lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

x,y = m(df['longitude'].values, df['latitude'].values)
m.scatter(x, y, s = 1, c = df['mag'], cmap = 'Reds', alpha = 0.5)
plt.title("Global Earthquake Locations")
plt.show()

