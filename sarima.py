import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the data
data = pd.read_csv('WISE4_BiologyEQRData.csv', encoding='ISO-8859-1', parse_dates=['phenomenonTimeReferenceYear'])

data.set_index('phenomenonTimeReferenceYear', inplace=True)

pd.set_option("display.max_columns", None)
data = data.dropna(subset=['resultEQRValue'])

# Fill missing values with the mean
data['resultEQRValue'] = data['resultEQRValue'].fillna(data['resultEQRValue'].mean())
# Perform seasonal decomposition
decomp = seasonal_decompose(data['resultEQRValue'], model='additive', period=12)

# Split the data into training and test sets
train_data = data.loc[:'2018-12-31']
model = SARIMAX(train_data['resultEQRValue'], order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit()

# Predict using the trained model
test_data = data.loc[data.index >= '2019', 'resultEQRValue']

preds = results.predict(start=test_data.index[0], end=test_data.index[-1])

# Fit the SARIMA model on the training data
model = SARIMAX(train_data['resultEQRValue'], order=(1,1,1), seasonal_order=(1,1,1,12))
model_fit = model.fit()

# Make predictions for the test data
# predictions = model_fit.forecast(len(test_data))

# Plot the predictions against the actual values
plt.figure(figsize=(10,6))
plt.plot(data.index, data['resultEQRValue'], label='Observed')
plt.plot(preds.index, preds, label='Predicted')
plt.legend()
plt.show()
# print(test_data)
# print(len(test_data))