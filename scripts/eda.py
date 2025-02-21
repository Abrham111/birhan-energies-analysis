import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Exploratory Data Analysis
def explore_data(df):
  print("Data Summary:\n", df.describe())
  print("Missing Values:\n", df.isnull().sum())
  
  plt.figure(figsize=(12, 6))
  plt.plot(df.index, df['Price'], label='Brent Oil Price')
  plt.title("Brent Oil Price Over Time")
  plt.xlabel("Date")
  plt.ylabel("Price")
  plt.legend()
  plt.show()
# Stationarity Check
def check_stationarity(df):
  result = adfuller(df['Price'])
  print("ADF Statistic:", result[0])
  print("p-value:", result[1])
  if result[1] < 0.05:
    print("The series is stationary.")
  else:
    print("The series is not stationary.")

  # ACF and PACF plots
  fig, ax = plt.subplots(1, 2, figsize=(12, 5))
  plot_acf(df['Price'], ax=ax[0])
  plot_pacf(df['Price'], ax=ax[1])
  plt.show()
