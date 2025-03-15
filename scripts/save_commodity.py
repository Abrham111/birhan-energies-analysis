import pandas as pd
import yfinance as yf

# Define commodities to fetch
commodities = {
    "Brent Oil": "BZ=F",
    "Crude Oil WTI": "CL=F",
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Natural Gas": "NG=F"
}

# Fetch historical data
def fetch_commodity_prices():
    all_data = {}

    for name, symbol in commodities.items():
        df = yf.download(symbol, start="2019-05-20", end="2022-11-14")

        # Debug: Print available columns
        print(f"Columns for {name}: {df.columns}")

        if df.empty:
            print(f"No data found for {name} ({symbol}). Skipping...")
            continue  # Skip empty data

        # Fix MultiIndex issue by selecting only the "Close" column
        if isinstance(df.columns, pd.MultiIndex):
            close_col = ("Close", symbol)  # MultiIndex tuple
        else:
            close_col = "Close"  # Single column case

        if close_col in df.columns:
            all_data[name] = df[close_col]
        else:
            print(f"Skipping {name} - No valid price column found.")
            continue

    # Combine into one DataFrame
    if all_data:
        commodities_df = pd.DataFrame(all_data)
        commodities_df.to_csv("../data/commodity_prices.csv")
        print("Commodity data saved to 'commodity_prices.csv'")
    else:
        print("No data fetched for any commodities.")

# Run the function
fetch_commodity_prices()
