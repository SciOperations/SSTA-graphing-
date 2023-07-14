import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as Nc4
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, filedialog


def day_of_year_to_date(year, day_of_year):
    date = datetime(year, 1, 1)
    date += timedelta(days=day_of_year - 1)
    return str(date)


def date_to_day_of_year(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_year = date_obj.timetuple().tm_yday
    return day_of_year


def sst_plot():
    lon_sst = a.variables['lon'][:]
    lat_sst = a.variables['lat'][:]
    anom = a.variables['anom']

    year_to_day = date_to_day_of_year(date_entry.get())
    m = Basemap(projection='mill', llcrnrlat=-30, urcrnrlat=30, llcrnrlon=180, urcrnrlon=290, lat_ts=20, resolution='c')
    plt.figure(figsize=(int(width_entry.get()), int(height_entry.get())))
    x, y = m(*np.meshgrid(lon_sst, lat_sst))
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    m.drawparallels(np.linspace(90, -90, num=10), linewidth=0.5, labels=[1, 0, 0, 1])
    m.drawparallels(np.linspace(0, 0, num=2), labels=[1, 0, 0, 1])
    m.drawmeridians(np.linspace(-180, 180, num=13), linewidth=0.5, labels=[1, 0, 0, 1])
    m.drawmapboundary(fill_color='white')
    m.fillcontinents(color='gray')
    color_scale = np.linspace(-6, 6, num=48, endpoint=True)
    color_scale1 = np.linspace(-6, 6, dtype=int, num=24, endpoint=True)
    m.contour(x, y, anom[year_to_day, :, :], 0, linewidths=0.5, colors='k')
    m.contourf(x, y, anom[year_to_day, :, :], color_scale, cmap=plt.cm.jet)
    plt.colorbar(orientation='horizontal', ticks=color_scale1)
    plt.xlabel('Deg C', color='black', fontsize=10.0, horizontalalignment='left', x=1.0, labelpad=25)
    plt.title("SSTA for: " + date_entry.get())
    plt.show()


# noinspection PyGlobalUndefined
def load_data():
    file_path = filedialog.askopenfilename()
    if file_path:
        global a
        a = Nc4(file_path, 'r', format="NetCDF4")


root = tk.Tk()
root.geometry('500x400')
root.title("SSTA Plot")

# Load Data Button
load_data_button = ttk.Button(root, text="Load Data", command=load_data)
load_data_button.pack(pady=10)

# Date Entry
date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")
date_label.pack()
date_entry = ttk.Entry(root)
date_entry.pack(pady=5)

# Width Entry
width_label = ttk.Label(root, text="Width:")
width_label.pack()
width_entry = ttk.Entry(root)
width_entry.pack(pady=5)

# Height Entry
height_label = ttk.Label(root, text="Height:")
height_label.pack()
height_entry = ttk.Entry(root)
height_entry.pack(pady=5)

# Plot the data by calling the function plot_sst
plot_data = tk.Button(root, text="Plot Data", command=sst_plot)
plot_data.pack(pady=10)

root.mainloop()
