from arch import arch_model
import matplotlib.pyplot as plt

def train_garch(df):
  # Fit GARCH(1,1) model
  model = arch_model(df['price'], vol='Garch', p=1, q=1)
  fitted_model = model.fit()
  print(fitted_model.summary())

  # Forecast volatility
  forecast = fitted_model.forecast(start=df.index[-30:])
  
  # Plot actual prices and predicted volatility
  plt.figure(figsize=(12, 6))
  plt.plot(df.index, df['price'], label="Brent Oil Price", color='blue')
  plt.plot(forecast.variance[-30:], label="Predicted Volatility", linestyle="dashed", color='red')
  plt.legend()
  plt.title("GARCH Volatility Forecast for Brent Oil Prices")
  plt.show()

