from arch import arch_model
import numpy as np
import matplotlib.pyplot as plt

def train_garch(df):
  # Rescale the Return values
  df['Return'] = df['Return'] * 100

  # Fit GARCH Model
  garch_model = arch_model(df['Return'].dropna(), vol='Garch', p=1, q=1)
  garch_fitted = garch_model.fit(disp='off')

  # Forecast Volatility
  forecast = garch_fitted.forecast(horizon=30)
  plt.figure(figsize=(12, 6))
  plt.plot(df['Date'].iloc[-100:], df['Return'].iloc[-100:], label='Returns')
  plt.plot(df['Date'].iloc[-30:], np.sqrt(forecast.variance.values[-1, :]), label='Volatility Forecast', color='red')
  plt.title("Volatility Forecast using GARCH")
  plt.legend()
  plt.show()

