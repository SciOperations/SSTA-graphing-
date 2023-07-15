# SSTA-graphing
Python app that will graph SSTA for meteorologists and oceanographers

This python script is for graphing SSTA (Sea Surface Temperature Anomaly) and the file format must be a NetCDF type. NetCDF stands for Network Common Data Form and its how data is stored in the file.
Data is accessed using arrays and with the aid of Numpy and matplotlib I created an application that can graph SSTA on a 2D map.

You will need to install these library dependancies to use this app:
numpy,
matplotlib,
netCDF4,
tkinter (should be installed with the Python application with the latest version)

NetCDF data can be downloaded from here: https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2.highres/catalog.html.
Choose sst.day.anom.[Year].nc


