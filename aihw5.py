# import pandas as pd
# import matplotlib.pyplot as plt

# # Load temperature data
# tmax_data = pd.read_csv('tmax.csv')  # Assuming this file contains the maximum temperature data
# tmin_data = pd.read_csv('tmin.csv')  # Assuming this file contains the minimum temperature data

# # Load ED admissions data
# ed_data = pd.read_csv('ed1.csv')

# # Ensure 'Date' columns are in datetime format
# tmax_data['date'] = pd.to_datetime(tmax_data['date'])
# tmin_data['date'] = pd.to_datetime(tmin_data['date'])
# ed_data['Week start date'] = pd.to_datetime(ed_data['Week start date'])

# # Merge temperature data
# temp_data = pd.merge(tmax_data, tmin_data, on='date', suffixes=('_max', '_min'))

# # Calculate average temperature
# temp_data['Average temperature (degC)'] = (temp_data['maximum temperature (degC)'] + temp_data['minimum temperature (degC)']) / 2

# # Replace 'n.p.' with 0 and convert the Count column to numeric
# ed_data['Count'] = pd.to_numeric(ed_data['Count'].replace('n.p.', 0), errors='coerce')

# # Filter for NSW jurisdiction and SA4 names containing 'Sydney'
# nsw_data = ed_data[(ed_data['Jurisdiction'] == 'NSW') & (ed_data['SA4 name'].str.contains('Sydney', case=False))]

# # Filter for 'Dehydration' condition
# dehydration_data = nsw_data[nsw_data['Condition group'].str.contains('Dehydration', case=False)]

# # Group by Week start date and sum the counts of 'Dehydration' condition
# total_counts_dehydration = dehydration_data.groupby('Week start date')['Count'].sum().reset_index()

# # Merge ED admissions data with temperature data
# merged_data = pd.merge(temp_data, total_counts_dehydration, left_on='date', right_on='Week start date')

# # Print merged data to verify
# print(merged_data.head())

# # Calculate correlations
# # Pearson correlation
# pearson_corr = merged_data[['Average temperature (degC)', 'Count']].corr(method='pearson')

# # Print Pearson correlation matrix
# print("Pearson Correlation Matrix:")
# print(pearson_corr)

# # Plot Average Temperature vs. ED Admissions Count
# plt.figure(figsize=(10, 6))
# plt.scatter(merged_data['Average temperature (degC)'], merged_data['Count'], alpha=0.5)
# plt.title('Average Temperature vs. ED Admissions Count for Dehydration')
# plt.xlabel('Average Temperature (°C)')
# plt.ylabel('ED Admissions Count')
# plt.grid(True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load temperature data
tmax_data = pd.read_csv('tmax.csv')  # Assuming this file contains the maximum temperature data
tmin_data = pd.read_csv('tmin.csv')  # Assuming this file contains the minimum temperature data

# Load ED admissions data
ed_data = pd.read_csv('ed1.csv')

# Ensure 'Date' columns are in datetime format
tmax_data['date'] = pd.to_datetime(tmax_data['date'])
tmin_data['date'] = pd.to_datetime(tmin_data['date'])
ed_data['Week start date'] = pd.to_datetime(ed_data['Week start date'])

# Merge temperature data
temp_data = pd.merge(tmax_data, tmin_data, on='date', suffixes=('_max', '_min'))

# Calculate average temperature
temp_data['Average temperature (degC)'] = (temp_data['maximum temperature (degC)'] + temp_data['minimum temperature (degC)']) / 2

# Replace 'n.p.' with 0 and convert the Count column to numeric
ed_data['Count'] = pd.to_numeric(ed_data['Count'].replace('n.p.', 0), errors='coerce')

# Filter for NSW jurisdiction and SA4 names containing 'Sydney'
nsw_data = ed_data[(ed_data['Jurisdiction'] == 'NSW') & (ed_data['SA4 name'].str.contains('Sydney', case=False))]

# Filter for 'Dehydration' condition
dehydration_data = nsw_data[nsw_data['Condition group'].str.contains('Dehydration', case=False)]

# Group by Week start date and sum the counts of 'Dehydration' condition
total_counts_dehydration = dehydration_data.groupby('Week start date')['Count'].sum().reset_index()

# Merge ED admissions data with temperature data
merged_data = pd.merge(temp_data, total_counts_dehydration, left_on='date', right_on='Week start date')

# Check for NaNs or infinite values and handle them
merged_data = merged_data.replace([np.inf, -np.inf], np.nan).dropna(subset=['Average temperature (degC)', 'Count'])

# Print merged data to verify
print(merged_data.head())

# Calculate correlations
# Pearson correlation
pearson_corr = merged_data[['Average temperature (degC)', 'Count']].corr(method='pearson')

# Print Pearson correlation matrix
print("Pearson Correlation Matrix:")
print(pearson_corr)

# Plot Average Temperature vs. ED Admissions Count for Dehydration
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['Average temperature (degC)'], merged_data['Count'], alpha=0.5)

# Add a trendline
try:
    # Check for minimum data points
    if len(merged_data) > 1:
        z = np.polyfit(merged_data['Average temperature (degC)'], merged_data['Count'], 1)
        p = np.poly1d(z)
        plt.plot(merged_data['Average temperature (degC)'], p(merged_data['Average temperature (degC)']), "r--")
    else:
        print("Not enough data to fit a trendline.")
except np.linalg.LinAlgError as e:
    print(f"Error fitting trendline: {e}")

# Customize the plot
plt.title('Average Temperature vs. ED Admissions Count for Dehydration')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('ED Admissions Count')
plt.grid(True)
plt.show()



