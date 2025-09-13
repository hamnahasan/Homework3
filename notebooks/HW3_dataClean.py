# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 21:59:50 2025

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'E:/0-PhD/Fall 25/DSE 511/Raw_Data.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Creating an empty dataframe from 1st Jan 1974 to 31st July 2025
date_range = pd.date_range(start='1974-01-01', end='2025-07-31', freq='D')
empty_df = pd.DataFrame({'DATE': date_range})

# Defining output directories seperately for each 4 meteorological stations
station_dataframes = {}


for station_id in df['STATION'].unique():
    # Filter data for the current station
    station_df = df[df['STATION'] == station_id]
    
    # Merging with the empty dataframe to align all dates
    merged_df = pd.merge(empty_df, station_df[['DATE', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'PRCP']], on='DATE', how='left')
    
    # Filling missing values in LATITUDE, LONGITUDE, and ELEVATION columns based on the station ID
    merged_df['LATITUDE'] = merged_df['LATITUDE'].fillna(station_df['LATITUDE'].iloc[0])
    merged_df['LONGITUDE'] = merged_df['LONGITUDE'].fillna(station_df['LONGITUDE'].iloc[0])
    merged_df['ELEVATION'] = merged_df['ELEVATION'].fillna(station_df['ELEVATION'].iloc[0])
    
    # Filling missing values in PRCP column with 0
    merged_df['PRCP'] = merged_df['PRCP'].fillna(0)
    
    # Saving cleaned data
    station_dataframes[station_id] = merged_df

# Separating each station data into a seperate csv file
for station_id, station_df in station_dataframes.items():
    output_path = f"{station_id}_cleaned.csv"
    station_df.to_csv(output_path, index=False)

### Calculating annual total precipitation and plotting them

annual_precipitation_sums = {}

# Calculate annual precipitation sum for each station
for station_id, station_df in station_dataframes.items():
    station_df['Year'] = station_df['DATE'].dt.year
    annual_sum = station_df.groupby('Year')['PRCP'].sum()
    annual_precipitation_sums[station_id] = annual_sum

## Plotting a combined graph 
plt.figure(figsize=(10, 6))

for station_id, annual_sum in annual_precipitation_sums.items():
    plt.plot(annual_sum.index, annual_sum.values, label=station_id)

# Adding labels and title
plt.title('Annual Precipitation Sum for Each Station (inches)')
plt.xlabel('Year')
plt.ylabel('Total Precipitation (inches)')
plt.legend(title='Station ID')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()