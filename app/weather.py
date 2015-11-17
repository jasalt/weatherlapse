# -*- coding: utf-8 -*-

# Parser for raw pywws weather data
# Raw data format order is: idx, delay, hum_in, temp_in, hum_out, temp_out,
# abs_pressure, wind_ave, wind_gust, wind_dir, rain, status.

from os import listdir

DATA_DIR = 'weatherstation/data/2015-07/'

filenames = listdir(DATA_DIR)

# TODO handle dates y/m/d
weather_data = {}

print("Reading weather data")

for fname in filenames:
    winds = []
    temps_out = []
    temps_in = []
    humidities = []
    with open(DATA_DIR + fname, 'r') as f:
        for line in f:
            cols = line.split(',')
            temps_in.append([cols[0], float(cols[3])])
            humidities.append([cols[0], float(cols[4])])
            temps_out.append([cols[0], float(cols[5])])
            winds.append([cols[0], float(cols[7])])
    day = int(fname[8:10])
    temperatures = [{'data': temps_out, 'name': 'Temperature outside'},
                    {'data': temps_in, 'name': 'Temperature inside'}]

    weather_data[day] = {}
    weather_data[day]['temp'] = temperatures
    weather_data[day]['wind'] = winds
    weather_data[day]['humid'] = humidities
