import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
data = pd.read_csv('WISE4_BiologyEQRData.csv', encoding='ISO-8859-1')
pd.set_option("display.max_columns", None)
data = data.dropna(subset=['resultEQRValue'])

# Convert the date column to a datetime object
# data['phenomenonTimeReferenceYear'] = pd.to_datetime(data['phenomenonTimeReferenceYear'])

# Set the date column as the index
data.set_index('phenomenonTimeReferenceYear', inplace=True)


# Perform seasonal decomposition
decomp = seasonal_decompose(data['resultEQRValue'], model='additive', period=12)

# Plot the original data, seasonal component, and residuals
fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(10, 8))
ax[0].plot(data['resultEQRValue'])
ax[0].set_title('Original Data')
ax[1].plot(decomp.seasonal)
ax[1].set_title('Seasonal Component')
ax[2].plot(decomp.resid)
ax[2].set_title('Residuals')
ax[3].plot(decomp.trend)
ax[3].set_title('Trends')
plt.tight_layout()
plt.show()

