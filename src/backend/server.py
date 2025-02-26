from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load and preprocess data
df = pd.read_csv('../../data/BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

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

if __name__ == '__main__':
    app.run(debug=True)