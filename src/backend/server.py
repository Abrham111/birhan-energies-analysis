from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load and preprocess data
df = pd.read_csv('../../data/BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

@app.route('/')
def welcome():
    return "Server running"

@app.route('/api/data')
def get_data():
   return jsonify({
        'dates': df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        'prices': df['Price'].tolist()
    })

@app.route('/api/summary')
def get_summary():
   return jsonify({
        'max_price': df['Price'].max(),
        'min_price': df['Price'].min(),
        'avg_price': df['Price'].mean(),
        'latest_price': df.iloc[-1]['Price']
    })

# Load commodity prices
commodity_df = pd.read_csv("../../data/commodity_prices.csv", parse_dates=["Date"])

# Merge datasets on Date
df = pd.merge(df, commodity_df, on="Date", how="inner")

# Compute full correlation matrix
correlation_matrix = df.corr()

@app.route("/api/correlation")
def get_correlation():
    return jsonify(correlation_matrix.to_dict())  # Return full matrix as JSON

@app.route("/api/predictions")
def get_predictions():
    df = pd.read_csv("../../data/lstm_predictions.csv")
    return jsonify(df.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)