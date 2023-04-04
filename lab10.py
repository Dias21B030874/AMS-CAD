import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("WISE4_BiologyEQRData.csv", encoding='ISO-8859-1')
pd.set_option("display.max_columns", None)

UID = data['UID']
versionId = data['versionId']
beginLifeSpanVersion = data['beginLifeSpanVersion']
monitoringSiteIdentifier = data['monitoringSiteIdentifier']
monitoringSiteIdentifierScheme = data['monitoringSiteIdentifierScheme']
parameterWaterBodyCategory = data['parameterWaterBodyCategory']
parameterNCSWaterBodyType = data['parameterNCSWaterBodyType']
observedPropertyDeterminandBiologyEQRCode = data['observedPropertyDeterminandBiologyEQRCode']
phenomenonTimeReferenceYear = data['phenomenonTimeReferenceYear']
parameterSamplingPeriod = data['parameterSamplingPeriod']
resultEcologicalStatusClassValue = data['resultEcologicalStatusClassValue']
resultNumberOfSamples = data['resultNumberOfSamples']
resultEQRValue = data['resultEQRValue']
resultNormalisedEQRValue = data['resultNormalisedEQRValue']
resultObservationStatus = data['resultObservationStatus']
remarks = data['remarks']
waterbaseObservationStatus = data['waterbaseObservationStatus']
waterbaseRemarks = data['waterbaseRemarks']

# Convert the "beginLifeSpanVersion" column to a datetime object
data["beginLifeSpanVersion"] = pd.to_datetime(data["beginLifeSpanVersion"])

# Set the "beginLifeSpanVersion" column as the index
data.set_index("beginLifeSpanVersion", inplace=True)

# Calculate the rolling average with a window size of 12 (i.e. 12 months)
rolling_avg = data["resultEQRValue"].rolling(window=12).mean()

#Plot the original data and the rolling average
fig, ax = plt.subplots()
ax.plot(data["resultEQRValue"], label="Original data")
ax.plot(rolling_avg, label="12-month rolling average")
ax.set_xlabel("Date")
ax.set_ylabel("EQR value")
ax.set_title("Trend analysis of contaminant concentrations")
ax.legend()
plt.show()
