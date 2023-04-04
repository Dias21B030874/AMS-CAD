import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Load the data
# from lab10 import phenomenonTimeReferenceYear

data = pd.read_csv('WISE4_BiologyEQRData.csv', encoding='ISO-8859-1')

# Remove missing values
pd.set_option("display.max_columns", None)
data = data.dropna(subset=['resultEQRValue'])

# Decompose the time series into trend, seasonal, and residual components
decomp = seasonal_decompose(data['resultEQRValue'], model='additive', period=12)


# Calculate the rolling average of the seasonal component
seasonal_roll_avg = decomp.seasonal.rolling(window=12, center=True).mean()


# Create a function to simulate the fate and transport of contaminants
def simulate_contaminants(years, trend_coef, seasonal_roll_avg, residual_coef):
    # Calculate the trend component of the time series
    trend = decomp.trend.iloc[-1] + np.arange(1, years * 12 + 1) * trend_coef

    # Calculate the seasonal component of the time series
    season = seasonal_roll_avg.values.repeat(years)[:years * 12]

    # Generate random noise for the residual component of the time series
    residual = np.random.normal(0, 1, size=years * 12) * residual_coef

    # Combine the components to get the simulated time series
    simulated = trend + season + residual

    return simulated


# Simulate 5 years of contaminant concentrations with trend_coef=0, season_coef=0, and residual_coef=1
# date_range = pd.date_range(start='1/1/2010', periods=60, freq='M')
simulated_data = pd.DataFrame({'resultEQRVal': simulate_contaminants(5, 1, 1, 1)})
simulated_data['phenomenonTimeReferenceYea'] = data['phenomenonTimeReferenceYear'].copy()

# # time_list = data['phenomenonTimeReferenceYear'].tolist()
# # simulated_data['time_list'] = time_list

# Create a new dataframe with the same structure as simulated_data
# date_range = pd.date_range(start='1/1/1970', periods=60, freq='M')
# new_data = pd.DataFrame({'phenomenonTimeReferenceYear': date_range,
#                          'resultEQRValue': np.random.rand(60)})
#
# # Add the list of dates to the new dataframe
# new_data['phenomenonTimeReferenceYear'] = phenomenonTimeReferenceYear
#
# # Plot the simulated and new data
# fig, ax = plt.subplots()
# simulated_data.plot(ax=ax, x='phenomenonTimeReferenceYear', y='resultEQRValue', label='Simulated data')
# new_data.plot(ax=ax, x='phenomenonTimeReferenceYear', y='resultEQRValue', label='New data')
# ax.legend()
# plt.show()

# dates = pd.date_range(start='1990', end='2015', periods=len(simulated_data))

# add dates to simulated_data dataframe
# simulated_data['dates'] = dates

# # Plot the original data and the simulated data
# ax = data.plot(x="phenomenonTimeReferenceYear", y="resultEQRValue", label='Original data')
# simulated_data.plot(x="phenomenonTimeReferenceYea", y="resultEQRVal", label='Simulated data')
# ax.set_xlabel('Date')
# ax.set_ylabel('EQR value')
# ax.set_title('Simulated contaminant concentrations')
# ax.legend()
# plt.tight_layout()
# plt.show()
# print(simulated_data.size)
# print(time_list.__sizeof__())
print(simulated_data)
# print(data['resultEQRValue'])

# fig, ax = plt.subplots()
# simulated_data.plot(ax=ax, x='phenomenonTimeReferenceYear', y='resultEQRValue', label='Simulated data')
# new_data.plot(ax=ax, x='phenomenonTimeReferenceYear', y='resultEQRValue', label='New data')
# ax.legend()
# plt.show()
