# -*- coding: utf-8 -*-

# Parser for raw pywws weather data
# Raw data format order is: idx, delay, hum_in, temp_in, hum_out, temp_out,
# abs_pressure, wind_ave, wind_gust, wind_dir, rain, status.

from os import listdir

DATA_DIR = 'weatherstation/data/2015-07/'

filenames = listdir(DATA_DIR)

daily_data = {}

print("Reading weather data")

for fname in filenames:
    winds = []
    temperatures = []
    with open(DATA_DIR + fname, 'r') as f:
        for line in f:
            cols = line.split(',')
            winds.append([cols[0], float(cols[7])])
            temperatures.append([cols[0], float(cols[5])])
    day = int(fname[8:10])
    data = [{'data': temperatures, 'name': 'Temperature C'},
            {'data': winds, 'name': 'Wind m/s'}]
    daily_data[day] = data
