import ruptures as rpt
import matplotlib.pyplot as plt

def detect_change_points(df):
  series = df['Price'].values
  algo = rpt.Pelt(model="rbf").fit(series)
  change_points = algo.predict(pen=10)

  # Plot results
  plt.figure(figsize=(12, 6))
  plt.plot(df.index, df['Price'], label="Brent Oil Price")
  for cp in change_points:
    plt.axvline(df.index[cp-1], color='r', linestyle="--", label="Change Point" if cp == change_points[0] else "")
  plt.legend()
  plt.title("Change Point Detection")
  plt.show()

  return change_points
